---
layout: post
title:  "Cheating in game simulations"
date:   2016-03-06 10:18:32 -0700
categories: programming
comments: true
---

# Intro

Suppose you're writing a simulation for a strategy game in which you'd like to compare how different strategies fare.  
You might require that the strategies satisfy an API like the following (in Go):

```
type Strategy interface {
    // Tell me what player i am, and tell me the initial board state
    initialize(view GameStateView, player int)
    // Decide what i should do, in a given game state
    decide(view GameStateView) Play
    // Process some game event out of the player's control, e.g. player's play
    process(view GameStateView, event Event)
}
```

## Problems

### 1. Out-of-band communication

This setup is fine for chess, but if the game involves partial information and the potential for collaboration (in my case, Hanabi), you can easily cheat:

```
var external_state *ExternalState = new(ExternalState)

type CheatingStrategy struct {
    internal_state *InternalState
}
func (s *CheatingStrategy) initialize(view GameStateView, player int) {
    s.internal_state = newInternalState(view, player)
}
func (s *CheatingStrategy) decide(view GameStateView) {
    // Perfectly fine code
    stuff := s.internal_state.get_stuff()
    decision := some_logic(view, stuff)
    // Cheat!  Read/mutate external state
    partner_cards := external_state.get_partner_cards()
    external_state.tell_partner(s.internal_states.my_cards)
    decision = changed_my_mind(view, partner_cards, decision)
    return decision
}
func (s *CheatingStrategy) process(view GameStateView, event Event) {
    // Could cheat here too
    ...
}
```

This cheating is possible because Go lets you have **shared mutable state**. It's the equivalent of bridge partners playing footsies under the table.

If the state weren't shared, it would be merely internal state, e.g. the inner workings of a bridge player's mind, which is fine.

If the state weren't mutable, it just means that Strategies may have fixed contracts ahead of time, e.g. bridge conventions.
But any nontrivial strategy will *automatically* have contracts with other instantiations of itself.
(I use bridge as an example, because it's clearly not considered cheating.
 But I've heard people argue this sort of thing is against the spirit of Hanabi.
 Could be - but I like the game more both theoretically and in practice when allowing it!)

### 2. Direct hacking attempt
Notice also, you can also attempt to cheat like this:

```
    // another attempt to cheat
    view.score += 1
```

So to be safe, the simulator shouldn't use the GameStateView after giving it away to the strategy.
This is likely to be an implementation annoyance and inefficiency, since the simulator will need to repeatedly produce deep copies of parts of the game state.

## Solutions

Obviously you can always cheat by storing things in a file or remote database.
So let's imagine an in-memory, network-less sandbox.
Interestingly, there are two quite different solutions.

### Solution 1: Functional programming

A pure functional language will make it much harder or impossible to cheat, by disallowing mutability. Here's the strategy API, in Haskell

```
class Strategy state where
    initialize :: Player -> GameStateView -> state
    -- Decide what player i should do, in a given game state
    decide :: Player -> GameStateView -> state -> (state, Play)
    -- Process some game event out of the player's control, e.g. player's play
    process :: Player -> GameStateView -> Event -> state -> state
```

Shared mutable state automatically became impossible, thanks to Haskell's purity!
The decide and process functions aren't allowed to have side effects.
As a bonus, mutating GameStateView became impossible, too.

Note: A Haskell proramming would actually probably not write it like this, but you get the point

### Solution 2: Rust

Until pretty recently, using a functional programming language might have been the only option. But along came Rust:

> Shared mutable state is evil. So functional programming languages thought: let's have no mutable state. So Rust thought: let's have no sharing of state.

Rust happens to be the language I was playing around with, for this Hanabi simulation business. Here's my strategy API:

```
pub trait Strategy {
    fn new(&GameStateView, &Player) -> Self;
    fn decide(&mut Self, &GameStateView) -> TurnChoice;
    fn update(&mut Self, &GameStateView, &Turn);
}
```

Again, shared mutable state becomes impossible[^1], thanks to Rust's ownership system!
And again, as a bonus, mutating the GameStateView becomes impossible - you have to have a mutable reference to do so.

[^1]: Okay. I lied - it's still possible, but made harder and highly discouraged. And you could tweak the language to disallow it (getting rid of Cell/Arc/Mutex), which is the important point.

For those interested, my project is [here](https://github.com/WuTheFWasThat/hanabi.rs)
