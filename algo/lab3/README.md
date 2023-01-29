

In this lab, implement `merge`.


## What is merge?

You are to write a function, `merge(left, right)`.  Both of its arguments are lists, and both of the argument lists may be assumed to be in pre-sorted order.  However, you have no idea if they are the same length (some of them might even be of length 0), or if everything in the left list is less than everything in the right list, or vice versa, etc.  Your function should return the result of combining both lists and sorting.

So for example:

```python
>>> merge([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
>>> merge([2, 4, 6], [1, 3, 5, 7])
[1, 2, 3, 4, 5, 6, 7]
>>> merge([], [])
[]
```



## How to cheat yourself


You know what's too easy?   This is too easy:

```python

def merge(left, right):
    return sorted(left + right)

```

This will pass all of the tests!  However.... there are a few reasons that this is too easy.

1. The reason we're looking at merge is so that we can use it in mergesort, so what's the point of a sort function that uses sort?
2. We can do it *asymptotically faster*.  Isn't that exciting?
3. Besides, it's *too easy*.  Live a little, break a sweat.


## So, what should I do?

Write merge the way we discussed it in class.

Over and over again, take the smallest element from each list, and put that into the output.

Do this without mutating or modifying the arguments (also without copying them and then modifying the copies).




### Fancy-pants extra credit

If you want to be fancy, you can do this without using `.append` or `.extend`.  Instead, you would pre-create the array with something like `ans = [None] * size` (after calculating the correct size), and then you'd assign into each slot as needed.  Apparently this is actually not more efficient in Python, but it is more efficient in many languages, and being able to do this is a little bit more swagger than doing it with `.append`.

PS: when I said "extra credit", I only meant that figuratively



## Also maybe time it

If you have suitable code left over from the timing lab(s), you could compare the "too easy" version (that just does `sorted(left + right)`) with your version.  How do they compare when you have two random lists of size 1000?  How do they compare on two random lists of size one million?  I found the answers kind of funny, personally.