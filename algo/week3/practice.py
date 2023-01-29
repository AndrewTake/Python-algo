# O(1), take first value in a list
# O(n) the time complexity depends on the input
# O(n) linear
# O(n^2) quadratic
# O(logn) when the input size gets smaller with each iteration
# O(n^2) when you perform a nested iteration
# O(2^n) growth rate doubles everytime you add to the input

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# In this example, the function takes in two arguments: an array arr and a target element target. It uses a for loop to iterate through the array, and checks if the current element is equal to the target element. If it is, it returns the index of the element. If the element is not found in the array, the function returns -1.

# You can also implement this algorithm using a while loop, or by using the in keyword or the list.index() method.

# It's worth noting that the time complexity of linear search algorithm is O(n) where n is the size of the array, which means it's not the best option if you are dealing with a large data set. Other searching algorithms like binary search has a time complexity of O(log n) which performs better on large data set.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# In this example, the function takes in two arguments: an array arr and a target element target. It uses a while loop that runs until low is less than or equal to high. It initializes low to 0 and high to the last index of the array. In each iteration, it calculates the middle index by taking the floor division of low and high and it checks if the element at the middle index is equal to the target. If it is, it returns the index of the element. If the element at the middle index is less than the target, it updates the low to the middle index + 1. If the element at the middle index is greater than the target, it updates the high to the middle index - 1.

# If the element is not found in the array, the function returns -1

# It's worth noting that in order to use binary search the array needs to be sorted, otherwise the algorithm will not work. Also, the time complexity of binary search algorithm is O(log n) which is more efficient than linear search, especially if the data set is large.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left and right arrays
    result.extend(left[i:])
    result.extend(right[j:])

    return result
