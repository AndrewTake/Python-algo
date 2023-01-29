

Okay, this is kind of a classic problem, and the solution is admittedly all over the internet, so I guess it's up to you if you want to cheat yourself of the experience.  Whether or not you've already heard of the riddle, I suggest you still do your best to implement it without looking up partial or complete existing solutions.  But hey, labs are ungraded, so do what you want to.


## Background

The problem goes like this.  You're helping out in a weightlifting gym, building a robot to move around the heavy plates.  In this (weird) gym, every plate has a different weight, and the weights are measured in kilograms, and so we can refer to the plates by using just their weight value (e.g. the plate that weighs 10kg, we just call that plate 10).  The plates are stacked, each plate lying horizontally, in piles.  To keep them stable, every plate must rest only on plates that are heavier than itself, so you can put a 3 (that is, a plate that weighs 3kg) on top of a 4 (that is, a plate that weighs 4kg), but not the other way around.  You can also put a 3 on top of a 5, and then you could stack a 1 on top of the 3 that's on the 5, that'd be fine.  There are exactly **three** places that weights can be stacked, call them "stack A", "stack B", and "stack C".

At any given time, we can list where all the weights are by listing the weights in stack A, then the weights in stack B, and then the weights in stack C.  The weights in each stack can be represented as a list of numbers, where the first number is the bottom weight.  So each list, the numbers should only go down.  Here are some legal examples:

```python
# 5 weights are all in stack B
([], [5, 4, 3, 2, 1], [])

# 3 weights are in stack A, 2 weights are in stack B, and no weights are in stack C
([5, 3, 1], [4, 2], [])

# almost all of the weights are in stack A, but one is in stack C
([4, 3, 2, 1], [], [5])

# again almost all the weights are in stack A, but one is in stack C
([5, 4, 3, 2,], [], [1])
```

Now here are some illegal arrangements:

```python
# cannot put a 2 on top of a 1
([3, 1, 2], [], [])

# and definitely cannot put a 5 on top of a 3
([], [], [4, 3, 5, 2, 1])
```

## Your Task, Standard Difficulty

Your job is to program the robot.  Again, your robot can only move one plate at a time, but it doesn't care how heavy the plate is (I guess it has a very strong arm but a very small hand or something).  And because the plates are in a pile, you may only move the top plate on any pile (i.e. the last number in the list).

And you don't *have* to solve this recursively, but wow it is easier.

At standard difficulty, we will assume that initially all the plates are in one stack, and you have been asked to move them all to another stack.  The problem is significantly easier if you may assume that all the plates start in one stack, so assume that.


You should print out a list of moves.  Perhaps your printout could look like this:

```
4 A -> B       ([5], [6, 4], [3, 2, 1])
```


### Hint about printing

<!-- You might do that printing-steps-out with code like this, assuming that you have appropriate variables for `movingPlate`, `fromPile`, `toPile`, and `stacks`: -->

```python
movingPlate = 4
fromPile = 0
toPile = 1
print(f"{movingPlate:>3} {'ABC'[fromPile]} -> {'ABC'[toPile]}       {stacks}")
```

But that code is just an idea, you could do it some other way.


### Hint about parameters

I suggest you make your function like this:

```python
def moveWeight(stacks, src, dst, numToMove=None):
    if numToMove == None:
        # the existence of numToMove is a hint about how I approached it
        numToMove = len(stacks[src])
    ## TODO: solve the rest of the problem
```

And then you could call it like this:

```python

# move all the weights from pile 0 (aka stack A) to pile 2 (aka stack C)
moveWeight(([5, 4, 3, 2, 1], [], []), 0, 2)

# that probably prints out a lot of moves to get the job done, like maybe 20 or 30 or something
```

### Hint about strategy - DEFINITELY READ THIS

I hope it's pretty clear that if you only need to move 1 disk, it's easy to do.

What if there were 2 disks on stack A and you needed to move them both to stack B, how would you do it?  What's the minimum number of moves you could use?  Come up with a solution by thinking about it, and write your solution down.  Don't code yet, just think.

Now, try to think of a way to solve this for 3 disks.  Can you use your 2-disk solution somehow?  Did your 2-disk solution use your 1-disk solution at all?

Again, this problem is *much* easier if you can spot how to do it with recursion.


### Example

So here is part of my solution's output when called as `moveWeight([[5, 4, 3, 2, 1], [], []], 0, 2)` (this is about 75% of the way through the solution):

```
  1 B -> A       [[3, 2, 1], [4], [5]]
  4 B -> C       [[3, 2, 1], [], [5, 4]]
  1 A -> C       [[3, 2], [], [5, 4, 1]]
```

## Bonus Task, Bonus Difficulty

If this was easy, here's a harder problem.  I don't know how much harder it is, because I haven't tried solving it.  I think it's not a lot harder, but I could be wrong, maybe it's really hard.

What if the plates do not all start on one stack?  What if they start scattered semi-randomly across the three stacks, and your job is to clean them all up and put them all on a particular stack?   You may still assume that they start in a legal arrangement (no upside-down stacks or anything dumb like that).  You must still keep them in legal arrangements at all times.

