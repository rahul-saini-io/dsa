def two_sum(a, t):
    # since I have to return numbers so I can use two pointers
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


a = [-10, 1, 11, -1, 6]
t = 10

print(two_sum(a, t))