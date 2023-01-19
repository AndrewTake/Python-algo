

Get some practice measuring things, and start to develop a sense for what things are slow.


## Basic Measuring

Use the code from the lecture, which I have partially included here.


```python


import statistics
import time


num_trials = 10000
times = []
some_values = list(range(100000))


for i in range(num_trials):
    before = time.time()

    # do something here that you want to measure

    after = time.time()
    difference = after - before
    times.append(difference * 1e9)

print("mean:", statistics.mean(times))
print("median:", statistics.median(times))
print("stdev:", statistics.stdev(times))

```


### Things to measure

Track your experiments in a table (just do something low-tech, like pen-and-paper, or a text file, nothing fancy is needed for now).

Here are some things you should try to measure:

* how long does it take to remove one element from the front of a list?
    * same question, but the end of the list.
        * same question but the *middle* of the list.
    * what about all of the above if this list is really big, like 10,000 elements?
* how long does it take to start with a list and add 1000 things to it, one at a time?
    * same thing, but what if the list already started with 10,000 things in it?  does it matter?
* what about doing a remove out of the middle of the list?
    * what about using pop to remove from the end of the list?
    * does the size of the list affect these?
* what about testing if something is in the list, like with `if thing in list_of_things:`
* try all of the above on a dictionary instead of a list...
    * are some things faster?  are some things slower?
    * are some things slower for small dictionaries but larger for big dictionaries, or vice versa?


Also, you and your partner have two different computers.  The times will probably not be the same.  How different are they?  Are they off by the same ratio in all cases, or is it more complicated than that?




## Bonus reading

If you got all that done, try reading this: https://www.peterbe.com/plog/how-to-do-performance-micro-benchmarks-in-python and see what he suggests, and how it is different from what we've already been doing.  I'm not necessarily saying it's worth the trouble; I'm just saying you could think about it.