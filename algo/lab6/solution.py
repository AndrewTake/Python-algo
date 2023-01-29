import math

# def merge(list1, list2):
#     '''
#     This is just a different way to do merge.
#     Do you like it?  Is it more fun to read?  Less fun to read?
#     '''
#     ans = [None] * (len(list1) + len(list2))
#     lists = [list1, list2]
#     indices = [0, 0]
#     indexAns = 0
#     flip = 0
#     while indices[0] < len(lists[0]) or indices[1] < len(lists[1]):
#         if indices[0] == len(lists[0]):
#             flip = 1
#         elif indices[1] == len(lists[1]):
#             flip = 0
#         elif lists[0][indices[0]] < lists[1][indices[1]]:
#             flip = 0
#         else:
#             flip = 1
#         ans[indexAns] = lists[flip][indices[flip]]
#         indexAns += 1
#         indices[flip] += 1
#     return ans


def merge(left, right):
    ans = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1
    return ans
    
    


def mergesort(list):
    # Solve this recursively.
    # You'll need at least one base case.  What's a good base case?  Do you need more than one?
    # You'll need at least one recursive case, and that recursive case will need at least one recursive call.
    # It's important that you divide-and-conquer, otherwise the big-O category won't be as good as it could be.
    # You *MAY* use slice before each recursive call.
    #   When you're done, try to figure out if slicing affects the big-O category of the solution.
    return list
