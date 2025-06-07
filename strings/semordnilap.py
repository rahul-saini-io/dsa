def semordnilap(array):
    """
        semordnilap are the words which are reverse for eg abc and cba
        so here we need to find if we reverse a word and it exists in the array
        we also need to handle same words like aaa. if we reverse and check it will say it reverse
        exists but it's same index word which also needs to be handle
        TC: O(nxm) SC: O(mxn)
    """
    array_set = set(array)
    res = []
    for word in array:
        rev = word[::-1]
        if rev in array_set and rev != word:
            res.append([rev, word])
            array_set.remove(word)
            array_set.remove(rev)

    return res


array = ['abc', 'cba', 'aaa', 'abc']
print(semordnilap(array))