r
* how long does it take to remove one element from the front of a list?
mean 142.669677734375
    * same question, but the end of the list.
mean 199.03182983398438
        * same question but the *middle* of the list.
mean 146.34132385253906
    * what about all of the above if this list is really big, like 10,000 elements?

* how long does it take to start with a list and add 1000 things to it, one at a time?
mean 91.43099999996824
    * same thing, but what if the list already started with 10,000 things in it?  does it matter?
mean 110.28700000010467
* what about doing a remove out of the middle of the list?
    * what about using pop to remove from the end of the list?
    * does the size of the list affect these?
* what about testing if something is in the list, like with `if thing in list_of_things:`
* try all of the above on a dictionary instead of a list...
    * are some things faster?  are some things slower?
    * are some things slower for small dictionaries but larger for big dictionaries, or vice versa?