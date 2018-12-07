---
layout: post
title:  "Smart TODO scheduling"
date:   2018-12-03
categories: productivity
comments: true
---

I would like an app where the main interface is extremely minimal: in big font, it tells me what I should do.

Whenever there's something I would like to do later, I simply speak to the app - it parses my request and reorganizes my schedule.

The app should be dead simple to use, and give you the best of todo lists, calendars, time-tracking apps, and more.

## Motivation: premeditated planning

In general, I often find myself with free time and no particular idea of what I should do.
On the other hand, occasionally I think of things which aren't habitual, but that I should be doing more of, e.g. calling my family.
But when the free time comes along, it takes much more effort to remember things I should be doing.
Ideally, I should premeditate about how I'd like to spend my time, and then later act faithfully on that without with low cognitive overhead.

You can imagine yourself in two possible modes, "CEO" and "worker".  Most time is spent in worker mode, doing things you decided in CEO mode.
(You might switch fluidly between the two modes, but ideally not too much.)
To facilitate this, we use software:  CEO me enters a list of tasks (and priorities and deadlines) into some app, and worker me repeatedly does *whatever the app says*.
The app is my boss, but since I program it, I'm my own boss.

## Advantages over existing solutions

Absorbing the functionality of both todo lists and calendars gives additional advantages.
Fundamentally, this is because both are tracking ways you should spend time.
Here are some examples:

- When I add an event, it can tell me what the marginal time would've been used for.  Is that acquaintance's birthday party really better than an hour of running or playing music? This is especially useful for people who tend to over-schedule themselves.
- There's less cognitive overhead if only using a single mechanism to decide what to do.  When I have todo list only for unstructured time, it's hard to make a habit of following it.  If that list is also your calendar, you might find it easier to stick to.
- It's easy to see overviews of your time spent, if it's all in one place.  So time-tracking comes nearly for free.

## Idealized interface details

Here's an idealized version of the app I imagine, at a high level.
I think it's quite hard to implement well, but there is a large spectrum of simpler versions.

### Basic actions

There are three main classes of actions, **Plan**, **Do**, and **Reflect**, corresponding to the life cycle of tasks.
The default screen is a "Do" screen.
You can prompt the app with queries to either plan new tasks or reflect on past tasks, in which case the app may show relevant information, such as a calendar.
When you exit a planning/reflecting session, it goes back to the "Do" screen.

#### **Plan**

You can add and edit tasks, in natural language, like:
- I'd like to sleep about 8 hours a day.  I never need more than 9 hours and always need at least 6
- I'd like to go for a 30 minute run on days with no other exercise planned, preferably in the morning.  Then I should shower right after.
- I should make an doctor's appointment every April and then enter the appointment time as a new task afterwards
- I'd like to get eggs and milk the next time I'm at the grocery store
- I have dinner with Bob on Friday at 6 PM, at his apartment
- Move my meeting with Eve to 8 PM
- I'd like to attend Saturday book club every other month, instead of every month
- Every day before sleeping, I should rate how happy my day was.
- I'd like to sleep 15 extra minutes per day, for the next 2 months.  In 2 months, set an event for me to compare happiness before and after.
- I'd like to reflect and plan my time every Sunday morning.

The app may ask clarifying questions, that you can optionally respond to.
- *How long do you take to shower?*
- *You're already busy on Friday 6 PM with Alice's birthday party.  Would you like to skip that?*

It can also just comment.
- *You will lose one hour of piano practice time.*

#### **Do**

There's a screen that tells you what to do.  You can either select Done or Skip.

If you mark the task "Done", you can optionally enter additional feedback/notes
- I was unable to finish this essay tonight.  It will take me another 2 hours or so.
- I finished this 15 minutes ago, and spent the last 15 minutes going to the gas station
- Alice's party was not as cool as I expected

If you "Skip", which is by default discouraged, you can/should enter a justification
- I only have 10 minutes before I'm getting picked up
- I'm at the mall, this task should be done at home
- I don't have the energy or willpower to exercise

#### **Reflect**

It's easy to query about tasks, which is useful during planning
- Show all planned exercise in the next month
- What are the next few times I plan to see either Alice or Bob?

And easy to query about time spent
- Show me a summary of time spent in the last week.
- Show me a graph of time spent exercising, week by week.
- What tasks do I skip often?
- What tasks do I want to do, but don't have time for?
- Show me tasks that took longer than I expected

### Bells and whistles

Obviously this app is not entirely fleshed out.  For example:

- You'd want integration with Google Calendar and have notifications for event-type items
- You should be able to attaching notes or subtasks to existing tasks
  - Add "buy bananas" to my shopping list
  - Add "Increase leisure time" to my next planning session
- It would be good to use location services in a smart way, if the user desires it

The list of feature requests is probably endless :)

## Conclusion

I would be very happy if someone implemented something like this.  If you are interested, please let me know!

Some suggestions for the name of such an app:
- Lachesis or Decima, the second of the Three Fates who measured and apportioned the thread of life.
- Remembear, in the spirit of Beeminder (if the Fates are too serious!)
