# Git Branching

## Information Gathering

- [learningitbranching](https://learngitbranching.js.org/?locale=en_US)
- [Git book](https://git-scm.com/book/en/v2)

## Commands

- Show all available commands
```
show commands
```

## Introduction Sequence

**Introduction to Git Commits**
***

- A commit is a snapshot of your files
- Only tracks "delta" of each file
- Think of commits as snapshots of the project

```bash
git commit
```

![git commit](/assets/learngitbranching/git-commit.png)

**Branching in Git**

- Pointers to a specific commit
- "branch early, and branch often"
- Include the work of this commit and all parent commits
- When modifying / commiting a branch, always switch over with `git checkout <name>`

```bash
git branch newImage
git checkout <name>
git commit

# Create branch and checkout
git checkout -b <name>
```

![git checkout](/assets/learngitbranching/git-branch.png)

**Merging in Git**

- How do we combine two branches together?
    - "merging" in git creates a special commit that has two unique parents
    - "I want to include all the work from this parent over here and this one over here, and the set of all their parents."
- When merging an ancestor into 'main', git simply moves the ancestor to 'main'

```bash
# On 'main' branch
git merge bufFix

# On 'main' branch
# Merge 'main' into 'bugFix'
git checkout bufFix; git merge main
```

![git merge](/assets/learngitbranching/git-merge.png)

**Rebase Introduction**

- Another way to combine work is to "rebase"
- Rebasing takes a set of commits, "copies" them, and plops them down somewhere else
- What is the difference between rebasing vs. merging?
    - Rebasing creates a nice linear sequence of commits.
    - This makes the commit log / history of the repository cleaner

```bash
# On 'bugFix' branch
git rebase main
git checkout main
git rebase bugFix
```

![git rebase](/assets/learngitbranching/git-rebase.png)

## Ramping Up

**Detach yo' HEAD**

- What is HEAD?
    - "HEAD" is the symbolic name for the currently checkout commit.
    - It's essentially what commit you're working on top of
- HEAD always points to the most recent commit in the working tree.
- What does it mean to detach HEAD?
    - Detaching HEAD just means attaching it to a commit instead of a branch.

```bash
git checkout C1
```

![git checkout](/assets/learngitbranching/git-head.png)

**Relative Refs (^)**

- You won't have commit tree visualization, so you'll have to use `git log`
- Commit hashes are long (ex. `fed2da64c0efc5293610bdd892f82a58e8cbc5d8`)
    - Fortunately, you only have to specify enough of the has until it uniquely identifies the commit
    - Typing `fed2` should be enough
- How do we navigate a sea of commit hashes?
    - "Relative refs" allow you to move between commits relative to where your current branch is.
    - Move upwards one commit at a time with `^`
    - Move upwards a number of times with `~<num>`

```bash
# Checkout to the first parent
# of main
git checkout main^

# Checkout to the second parent
# of main (grandparent).
git checkout main^^

git checkout C3             # HEAD at C3
git checkout HEAD^          # HEAD at parent of C3
git checkout HEAD^          # HEAD at grandparent of C3
git checkout HEAD^          # HEAD at great-grandparent of C3
```

![relative ref](/assets/learngitbranching/git-relative-ref.png)

**Relative Refs #2 (~)**

- What happens if you have a commit that is several (or hundreds) of commits away and you don't want to type of `^` a bunch of times?
    - Git also has a `~` operator which takes a trailing number that specifies the number of parents you would like to ascend.
- What are the use cases for relative branching?
    - One of the most common uses of relative refs is to move branches around
    - Reassign a branch to a commit with `-f` option

```bash
git checkout HEAD~4
git branch -f main HEAD~2
```

![git relative ref 2](/assets/learngitbranching/git-relative-ref-2.png)

**Reversing Changes in Git**

- What happens if I accidentally make a change in Git or do something I didn't intend?
    - There are two primary ways to undo changes in Git: `git reset` and `git revert`
- `reset` reverses changes by moving a branch reference backwards locally.
    - This moves you back to the previous commit

```bash
git reset HEAD~1
```

![git reset](/assets/learngitbranching/git-reset.png)

- `revert` reverses changes and shares those changes with others.
    - This creates a new commit and moves the branch forward.
    - This is because the new commit introduces changes by changing what is current with what was previous.

```bash
git revert HEAD
```

![git revert](/assets/learngitbranching/git-revert.png)

## Moving Work Around

**Cherry-pick Intro**

- "I want this work here and that work there"
- How do you select / sort specified work into a single commit?
    - `cherry-pick` is a way of copying a series of commits below your current location.

```bash
git cherry-pick <Commit1> <Commit2> <...>
```

![git cherry-pick](/assets/learngitbranching/git-cherry-pick.png)

**Interactive Rebase Intro**

- What happens when you don't know the set of commits you want to `cherry-pick`?
    - Interactive rebasing allows you to pick a series of commits you're about to rebase.
- To use the interactive rebase, use the `-i` with the rebase command
- This will open up a text editor which'll allow you to choose and reorder commits

```bash
git rebase -i HEAD~4
```

## A Mixed Bag

**Grabbing Just 1 Commit**

- Here's a common situation:
    - You are attempting to track down a bug. To aid in your detective work, you put in a few debug commands and a few print statements. All of the debugging / print statements are in their own commits. Finally I track down the bug, fix it, and rejoic! Only problem is that I now need to get my `bugFix` back into the `main` branch. If I simply fast-forwarded `main`, then `main` would get all my debug statements which is undeseriable.
- You can use either `git rebase -i` or `git cherry-pick` in order to update `main` with only the changes made in `bugFix`.

```bash
# On 'main' branch
git cherry-pick C4
```

![grabbing just 1](/assets/learngitbranching/git-grabbing-just-1.png)
