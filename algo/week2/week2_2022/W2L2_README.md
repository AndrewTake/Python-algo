

## Introduction

This lab is about mergesort, and it is fundamentally divided into two parts:

* A) implement a merge function; we'll call it `merge`
* B) use this to implement bottom-up merge sort, perhaps with some shortcomings or limitations


## Merge In Place

First, our goal is to implement `merge`.

Conceptually, a merge function is pretty simple, and we covered it in lecture.  It takes in two sorted lists, and combines them to produce a single sorted list, by just looking at the front of each of the input lists, and choosing whichever has priority, until it is finished.

<img src="./merge_illustrated_scaled.png"></img>
![merge_illustrated_scaled](https://user-images.githubusercontent.com/91557490/189853577-857e54aa-c000-45c5-96ca-291f3ad48761.png)

There are different ways to organize the merges in a merge-sort, and how they're organized will affect the *details* of writing the merge function.  I have tried to make a choice here that will make your life easier, but I think that at first it will look more complicated, so stay calm and carry on.

(If you get to the end of this and you're bored, you can think about how to mess with the way it all fits together and see if you can make it better or worse or whatever.)


```python
def merge(overall, run1_from, run1_to, run2_from, run2_to):
    pass
```

The version of merge that I am defining here works on a single larger list, and chooses some *sub-lists* of that list and merges those, and then puts those merged sub-lists back where they came from in the larger list.  I know that's a bit confusing, so there are examples below.

* The first parameter is a list, the list you're going to modify.
* The second and third parameters define the first sub-list that is already sorted.  This will be defined with a half-open interval, like Python slice syntax, so if `run1_from` is 8 and `run1_to` is 12, then the indices that are part of the first sub-list will be 8, 9, 10, and 11, but **not 12**.
* Similarly, the fourth and fifth parameters will define the second sub-list, which also should be already sorted.
* The return value will be the resultant list with the sub-lists merged

Note that your function **must** *return the modified list*.  It **may also** *modify the input list in place*; this is optional but permitted.

You can see two examples below.  If they're not clear, please help me figure out how to make it clearer!

So that's it, that's your job.  Implement this `merge` function, please.


### Example 1

Consider this data:

```python
>>> groups_of_four                 # this is an array in which each 4-some of values are sorted, even though the entire list is not
[62, 66, 83, 96, 20, 36, 77, 97, 57, 59, 80, 92, 13, 87, 90, 91, 16, 51, 53, 61]
>>> groups_of_four[4:8]            # aha, the [4:8] slice is ordered
[20, 36, 77, 97]
>>> groups_of_four[8:12]           # aha, the [8:12] slice is ordered
[57, 59, 80, 92]
>>> merge(groups_of_four, # notice that the function does *return* its answer (this is required)
[62, 66, 83, 96, 20, 36, 57, 59, 77, 80, 92, 97, 13, 87, 90, 91, 16, 51, 53, 61]
>>> groups_of_four                 # also notice that the original variable has also been modified (this is optional)
[62, 66, 83, 96, 20, 36, 57, 59, 77, 80, 92, 97, 13, 87, 90, 91, 16, 51, 53, 61]
>>> groups_of_four[4:12]           # and after the function call, the [4:12] slice is the result of merging [4:8] with [4:12]
[20, 36, 57, 59, 77, 80, 92, 97]
```

Notice that we used `merge(groups_of_four, 4, 8, 8, 12)` to merge the `[4:8]` slice with the `[8:12]` slice.  It's as if we took those two slices out, merged them into one array, and then put that merged array back into the place we got the slices from.

### Example 2

Here is a different example, with pre-sorted chunks of length 3 instead of pre-sorted chunks of length 4.


```python
>>> groups_of_three
[6, 13, 18, 3, 10, 19, 2, 4, 17, 5, 8, 9]
>>> after_first = merge(groups_of_three, 0, 3, 3, 6)
>>> after_first
[3, 6, 10, 13, 18, 19, 2, 4, 17, 5, 8, 9]
>>> after_second = merge(groups_of_three, 6, 9, 9, 12)
>>> after_second
[3, 6, 10, 13, 18, 19, 2, 4, 5, 8, 9, 17]
>>> all_done = merge(groups_of_three, 0, 6, 6, 12)
>>> all_done
[2, 3, 4, 5, 6, 8, 9, 10, 13, 17, 18, 19]
```



## Bottom-up Merge Sort

Okay, how can we use this merge to implement a sorting function?

There are (at least) two fundamentally different approaches, and this week we're going to look at doing it "bottom up", which means that we don't really look at the whole entire problem until the very end.  (This isn't really the most typical way of looking at mergesort, it's just our challenge for this week.)

At the beginning, an unsorted list can be regarded as a bunch of smaller lists, each of size 1, each sub-list is sorted (becaue how can a size-1 list be unsorted?), but not sorted-as-a-whole.  We can merge the size-1 lists into sorted size-2 lists, and then merge the sorted size-2 lists into sorted size-4 lists, and so on, until we have sorted the entire list.

So, your job is to do that.  Implement `merge_sort_bottom_up(list)`.  Much like your `merge`, you will return the sorted list.  Much like your `merge`, you **may** also mess with the input list, rearrange it in place.

Really, tackle this however you like.  However, I have a strategy suggestion.

* First, assume that your input list will always have exactly 16 elements.  Solve this.
    * the only test that this will pass is probably `test_mergesort_sixteen`, that's your milestone
* Then, extend your logic so that your input list could have 0 or 1 or 2 or 4 or 8 or 16 elements.
    * you should now pass `test_mergesort_eight` plus several of the tests from before
* Then, extend your logic so that your input list could have any number up to 16 elements.
    * realistically this probably passes every test in my suite except `test_mergesort_31`
* Then, extend your logic so that your input list can have any number of elements (up to the reasonable limits of your computer's RAM, of course, so 10000 is fine, who cares).

The unit tests that I am giving you are organized assuming that you do things this way.  But if you think my advice is bad, you may ignore it.

However, I do have one catch.  If you know how to do mergesort recursively (top-down), we're not doing that this week (we'll look at it later).  So this week, challenge yourself to do it bottom-up.

