
## Introduction


In this lab we're going to practice turning algorithms into programs, and we're also going to review some of the simple-and-mediocre sorts from the lecture.

So you should implement `selection_sort` and then `insertion_sort`.


## Ground Rules

First of all, to many people, reviewing their first lab, I said something like "in general, modifying input parameters is a good way to create bugs, and I want you to be aware of that".  This is good general advice, and I stand by it, but we are *ignoring that guideline* in this lab.  You will absolutely modify the data given to you, and you will not return anything.  Again, this is not really good advice for normal software engineering, but oh well.

Next, although you could do this all sorts of ways, I have a particular strategy in mind that I would like you to follow.  I want you to build your sorts around the `swap` function that I have provided.  So your code should work by using loops and conditionals to decide when to swap, and when not to swap, and when to be finished.

Note that this swap function takes two *indices* as arguments.  Experiment with it if you need to.


## How To Run The Tests


You can run the tests for each of the sort functions with the following commands:

```bash
python -m unittest -v test_1_selection_sort.py
python -m unittest -v test_2_insertion_sort.py
```

(As always, whether you need `python` or `python3` will depend on how you installed it, and that's your business.)

If you don't specify a particular tests file, it'll run all of them.  Which will probably be a pain in the butt.


## Catches

### (a.k.a. my tests are bad)

This section really is just a list of ways that you could do less work, and why I think you shouldn't.

First, my tests cannot tell if you do them differently from each other.  So if you do one of them, you can just copy-paste the code and rename it, and the tests will pass.  Obviously doing that is like going to the gym and lifting inflatable air-filled weights.  You might impress me with how fast you finish the lab, but you're not getting any stronger.

Second, actually, if you're going to cheat yourself, you can cheat yourself even faster by just using the python built-in sorting functions, right?   Either `list.sort()` or `sorted(list)`.  So, again, maybe don't.

Third, python implementations of these sorts are all over the internet, so copy-pasting off the internet is even easier for this assignment than for some things.  And, again, that's just cheating yourself.  My advice is to avoid reading implementations in Python.  If the description in lecture wasn't clear enough, then try to start with reading only English descriptions (or any other non-programming language if you prefer), and if necessary read pseudocode, or maybe code in languages that are different from Python.




## Bonus

If you did all that, you might as well do bubblesort too.  It's dumb, but it's traditional.

```bash
python -m unittest -v test_3_bubble_sort.py
```
