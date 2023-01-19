
## Introduction

Hello, good day, how are you?

In this lab we're going to practice turning algorithms into programs, and we're also going to review some of the simple-and-mediocre sorts from the readings.

So your job is to implement as many as you can of the following: `selection_sort`, `insertion_sort`, `bubble_sort`.

Honestly, that's basically the whole README, but there are some catches/gotchas.

## How To Run The Tests


You can run the tests for each of the sort functions with the following commands:

```bash
python3 -m unittest -v test_1_selection_sort.py
python3 -m unittest -v test_2_insertion_sort.py
python3 -m unittest -v test_3_bubble_sort.py
```

(If you installed Python as `python`, then change that part from `python3` in the command.)

If you don't specify a particular tests file, it'll run all of them.

## Catches (a.k.a. my tests are bad)

This section really is just a list of ways that you could do less work, and why I think you shouldn't.

First, my tests cannot tell if you do them differently from each other.  So if you do one of them, you can just copy-paste the code and rename it, and the tests will pass.  Obviously doing that is like going to the gym and lifting inflatable air-filled weights.  You might impress me with how fast you finish the lab, but you're not getting any stronger.

Second, actually, if you're going to cheat yourself, you can cheat yourself even faster by just using the python built-in sorting functions, right?   Either `list.sort()` or `sorted(list)`.  So, again, maybe don't.

Third, python implementations of these sorts are all over the internet, so copy-pasting off the internet is even easier for this assignment than for some things.  And, again, that's just cheating yourself.  My advice is to avoid reading implementations in Python.  Try to start with reading only English descriptions (or any other non-programming language if you prefer), and if necessary read pseudocode, or maybe code in languages that are different from Python.


So that's pretty much it.  See how many you can get done!