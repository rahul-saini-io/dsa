def common_char(words_arr):
    """
        return char/chars that are common in all the words of the array
        :param words_arr: ["abc", "bcd", "cbaccd"]
        :return: ["b", "c"]
        TC = O(mxn)
        SC = O(c) => c is the no of uniq char across strings
    """
    f_map = {}
    n = len(words_arr)
    res = []
    for word in words_arr:
        uniq_word = set(word)
        for ch in uniq_word:
            if ch in f_map:
                f_map[ch] += 1
            else:
                f_map[ch] = 1

    for k, v in f_map.items():
        if v == n:
            res.append(k)

    return res


words_arr = ["abc", "bcd", "cbaccd"]

print(common_char(words_arr))