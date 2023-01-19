def swap(arr, index_a, index_b):
    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]

# dont use classes

# python3 -m unittest -v test_1_selection_sort.py
# python3 -m unittest -v test_2_insertion_sort.py
# python3 -m unittest -v test_3_bubble_sort.py

# def selection_sort(arr: list(int)) -> list(int):
#     value = 0
#     while value < (len(arr)):
#         target = arr[value]

#         swap(arr, value, arr.index(min(target)))


def selection_sort(arr: list[int]) -> list[float]:
    """Selection sort works by taking the very first element in an array and comparing it to the elements in the rest of the array one by one. If the element in the array is smaller, it gets swapped with the first array. 
    We start with the far left value, and 1 by 1, compare every value in the unsorted list to it. if we find a value that is smaller, we add it to the sorted list. 

    2 4 1 5  
    2 | 4 1 5  

    in this example, 2 is compared to several numbers: 4, 1, and 5. 
    1 is smaller than 2, they swap places. 

    1 4 | 2 5 

    Next we compare the second value in the sorted list, to every value in the unsorted list.
    4 is compared to 2 and 5. 
    2 is smaller than 4. 
    2 and 4 swap. 

    1 2 | 4 5
    1 2 4 | 5
    1 2 4 5

    This continues until the array is ordered."""

    for i in range(0, len(arr) - 1):
        # range from 0 to len(arr), you can also do range(0,len(arr) -1. Becuase once youve gone through the range, and swapped all variables, you can assume that the last variable is in place, and dosnt need to be changed.

        min_value = i
        # we want the the first element in the array to be the default min value.

        for j in range(i + 1, len(arr)):
            # a second loop: think of a line with each value represented, (1,2,5,6,8,4)
            # the min value, i, is the first element. you need to do i+1 to get every value after i in the array.

            if arr[j] < arr[min_value]:
                # if we find a value that is smaller than the min value. We swap their positions by saying the min value index is equal to the smallest values index.
                min_value = j

        if min_value != i:
            #  we check if the min value is not the current index of the array.
            arr[min_value], arr[i] = arr[i], arr[min_value]
            # this is the syntax to swap positions. We swap the min value index with the current range index.
    return arr


def insertion_sort(arr):
    """Insertion sort works by having two lists. A sorted list and an unsorted list. The first element in the arr is added to the sorted sublist. We then add a number to the sorted list that is positionally on the immediate right of the first number in the sorted list. We compare the number added - to the number on its immediate left. If the number added is smaller, we swap the numbers. The number added will continue to swap places in the sorted list until it finds a number that is smaller than itself. 

    1 2 4 3 7 6 5  
    1 | 2 4 3 7 6 5
    1 2 | 4 3 7 6 5

    We take the item that is right to the first item, and add it to the sorted list.
    We then compare if the item that has been added is smaller or larger than the original item.
    In this case, the item added is larger than the original item, so there is no swap needed.

    1 2 4 | 3 7 6 5
    1 2 4 3 | 7 6 5

    3 was added to the subarray. 3 is smaller than 4, and therefore needs to be swapped.

    1 2 3 4 | 7 6 5
    1 2 3 4 7 | 6 5
    1 2 3 4 7 6 | 5
    1 2 3 4 6 7 | 5
    1 2 3 4 6 5 7
    1 2 3 4 5 6 7    

    we continue sorting the array until the it is in order. 
    """

    length_index = range(0, len(arr))
    # find the range of the indexes that you need to loop through

    for i in length_index:
        value_sort = arr[i]
        # set a value to equal indices in an array

        while arr[i-1] > value_sort and i > 0:
            # i > 0 because python allows for negative indexing, if there was a negative index python would return a value from the end of the array

            arr[i], arr[i-1] = arr[i-1], arr[i]
            # swap
            i = i - 1
            # we look at the next item by using i = i-1

    return arr


def bubble_sort(arr):
    """Bubble sort works by comparing two indices in an unsorted list. The first element in the arr is compared to the second element in the array. When every item in the array has been swapped, the loop iterates, and every item in the arr is swapped a second time. This continues until every item in the arr is in ascending order of values. 

    1 2 4 3 7 6 5  
    1 2 | 4 3 7 6 5
    1 | 2 4 | 3 7 6 5
    1 2 | 4 3 | 7 6 5  

    4 is larger than 3, they swap

    1 2 3 4 | 7 6 | 5

    7 is larger than 6, they swap

    1 2 3 4 6 | 7 5 |

    7 is larger than 5, they swap

    1 2 3 4 | 6 5 | 7 

    5 is smaller than 6, they swap

    1 2 3 4 5 6 7 
    """
    index_length = len(arr) - 1
    #  we take the length of the array -1. We subtract 1 because bubble sort compares the number next to it. If you are the last indice of an arr, there is nothing you can compare yourself to.
    sorted = False
    # we set a check to see if the list has been sorted

    while not sorted:
        # if the list has not been sorted, enter the loop
        sorted = True
        # once we enter the loop, we know the list is in progress of being sorted, and will be sorted. Therefore, we set the boolean to True.

        for i in range(0, index_length):
            # this forloop holds the logic of the sort
            if arr[i] > arr[i+1]:
                # if the value in the arr is greater than the value to the right of it, we neeed to swap places. The value on the left always needs to be smaller than the value on the right.

                sorted = False
                # if the program enters this statement. We know that the arr hasnt been sorted yet, because a value to the right of the smallest value is larger. We put sorted as false to alert the program that it is not finished sorting.
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # this statement contains the logic for the sort.
    return arr
