def cypher(s, key):
    res = ""
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    for ch in s:
        ch_idx = alpha.index(ch)
        if ch_idx + key > 25:
            ch_idx = (ch_idx + key) % 26
            res += alpha[ch_idx]
        else:
            res += alpha[ch_idx + key]

    return res


s = "xyz"
key = 2

print(cypher(s, key))