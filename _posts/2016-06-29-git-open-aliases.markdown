---
layout: post
title:  "Git 'open' aliases"
date:   2016-06-29 10:18:32 -0700
categories: programming git productivity
comments: true
---

Recently, I made some aliases for opening files within a git repo.

They're pretty simple, but they've affected my workflow a lot - I nearly never open files *without* using a git alias anymore.

After explaining to a coworker what the git commands "mop" and "shop" meant, they said I should share these with others.
Though I'm sure someone else has thought of this, a quick Google search didn't turn up anything.  So here they are!

```
# These go in your .gitconfig under the [alias] heading

# open file by name
op = "!f() { $(git editor) $(git ls-files | grep -i \"$@\"); }; f"

# open currently edited (unstaged) files
eop = "! $(git editor) $(git ls-files --modified)"

# open files for conflicts (good for rebase/cherry-pick/merge)
mop = "!f() { $(git editor) $(git diff --name-only --diff-filter=U); }; f"

# open files present in diff
dop = "!f() { $(git editor) $(git diff --name-only $@); }; f"

# grep and open files containing
gop = "!f(){ $(git editor) $(git grep --name-only \"$@\"); }; f"

# "show and open" commit
shop = "!f() { $(git editor) $(git show --pretty=\"format:\" --name-only $1); }; f"

# open on github (requires hub)
hop = "!f() { hub browse -- blob/master/$(git find $@ | head -n 1); }; f"

# fuzzy aliases require fzf (added 2016/8/12)

# fuzzy open by name, takes no argument
zop = "!f() { \
  local file=$(git ls-files $(git rev-parse --show-toplevel) | fzf -m); \
  if [[ -z $file ]]; then return 1; fi; \
  $(git editor) $file; \
}; f"

# fuzzy grep (does only one file), takes no argument
zgop = "!f() { \
  local raw_selection=$(git grep -n '.*' | fzf); \
  if [[ -z $raw_selection ]]; then return 1; fi; \
  local selection=${raw_selection%:*}; \
  local file=${selection%:*}; \
  local line=${selection##*:}; \
  $(git editor) +\"$line\" \"$file\"; \
}; f"

editor = config --get core.editor
```

NOTE: These aliases only work with editors that take separate filenames as arguments and opens all of them.
I think vim and emacs both work though, so that should cover many users.

For those curious, my full list of aliases can be found [here](https://github.com/WuTheFWasThat/dotfiles/blob/master/.gitconfig).
Please let me know if you have other useful git aliases!
