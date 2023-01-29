
## Your Task

Implement mergesort using recursion.

I have included for you an implementation of `merge`.  It accepts two sorted lists as parameters, and returns the result of merging them.

Your mergesort *may* modify the input, although I don't think you really have any reason to.  Your mergesort *must* return the sorted list.


## The Explanation

How do you do recursive mergesort?

First of all, you need a base-case.  I am going to leave that to you to figure out.

Then, in the recursive case, you simply:
* cut the list in half
* sort each half
* merge 'em

You may use slice.  It does have the disadvantage of increasing memory usage, but it turns out that mergesort always has some version of this problem (though it can be made less bad than what happens if you just use slice).  It's worth contemplating how *much* extra memory it uses up, and also it's worth contemplating whether it increases the time cost of the whole sort (especially whether it increases the big-O category of the time cost).




## Side Quest

Is it possible to do mergesort without recursion?  I'll tell you: it is possible.  Can you figure it out?  Warning, I personally think it's much harder.  And there's no point in looking this up online, you won't learn anything that way.
