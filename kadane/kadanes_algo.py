def kadane_algo_approach1(a):
    """ here we need to find max sum of subarray."""
    # approach 1
    max_sum = a[0]
    n = len(a)
    curr_sum = a[0]

    for i in range(1, n):
        val = a[i]
        curr_sum = max(val, curr_sum+val)
        max_sum = max(curr_sum, max_sum)

    return max_sum

def kadane_algo_approach2(a):
    """ here we need to find max sum of subarray."""
    # approach 2
    max_sum = a[0]
    n = len(a)
    curr_sum = a[0]

    for i in range(1, n):
        val = a[i]
        if val < curr_sum + val:
            curr_sum = curr_sum + val
        else:
            curr_sum = val

        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


a = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadane_algo_approach1(a))
print(kadane_algo_approach2(a))