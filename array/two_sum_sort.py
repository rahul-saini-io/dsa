"""
    Here output will be values not index so we can sort and use two pointers technique
"""


def two_sum_sort(array, target):
    # sort array inplace
    array.sort()
    # [-1, 0, 5, 6, 6, 12, 17]
    # take two pointers i & j
    i, j = 0, len(array)-1

    while i<j:
        sum = array[i] + array[j]
        if sum < target:
            i+=1
        elif sum > target:
            j-=1
        else:
            return [array[i], array[j]]

    return []


array = [-1, 6, 5, 0, 17, 6, 12]
target = 12

print(two_sum_sort(array, target))