def first_non_rep_char(word):
    f_map = {}
    for ch in word:
        f_map[ch] = f_map[ch]+1 if ch in f_map else 1

    """
        In python 3.7+ dict maintains insertion order so iterate over dict can also give correct answer but we are
        but in interview we need more common approach so we iterate of word again to check the order.
    """
    for ch in word:
        if f_map[ch]==1:
            return ch

    return -1


word = "abcddca"
print(first_non_rep_char(word))