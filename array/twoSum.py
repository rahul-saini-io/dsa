def two_sum(a, t):
    # since I have to return numbers, so I can use two pointers
    a.sort()
    # -10, -1, 1, 6, 11
    i, j = 0, len(a)-1

    while i<j:
        if a[i] + a[j] == t:
            return [a[i], a[j]]
        elif a[i] + a[j] < t:
            i+=1
        else:
            j-=1

    # no pair found
    return []


def two_sum_map(a, t):
    # since I have to return indexes, so will use map

    map = {}
    for i, num in enumerate(a):
        if (t-num) in map:
        # we got are pairs return indexes
            return [map[t-num], i]
        # store num with it's index
        map[num] = i
    return []

a = [-10, 1, 11, -1, 6]
b = [-10, 1, 11, -1, 6]

t = 10

print(two_sum(a, t))
print(two_sum_map(b, t))