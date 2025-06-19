
"""
    find 2 indexes whose value's sum = target
    Note: since we want indexes as output so we cannot sort and use two pointers here

    TC: O(n) n is size of array
    SC: O(n) n is size of array and because we are using extra dictionary/map

"""

def two_sum(array, target):
    diff_map = {} # -1:0, 6:1, 5:2, 0:3, 17:4
    for i, val in enumerate(array):
        diff = target - val
        if diff in diff_map:
            return [i, diff_map[diff]] # [5,1]
        else:
            diff_map[val] = i
    return [] #


array = [-1, 6, 5, 0, 17, 6, 12]
target = 12

print(two_sum(array, target))