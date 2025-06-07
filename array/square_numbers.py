def square_no(a):
    # sort inplace if not already
    a.sort()
    i, j = 0, len(a)-1
    # this k index will be used to fill result array from last idx, then second last idx and so on to first idx
    k = len(a)-1

    # result array O(n) space. Initialize array equal to len of given array
    res = [0] * len(a)
    while i<=j:
        if abs(a[i]) < abs(a[j]):
            res[k] = a[i]*a[i]
            i+=1
        else:
            res[k] = a[j]*a[j]
            j-=1
        k -= 1
    return res

a = [-5,-4,0,-2,-1]

print(square_no(a))