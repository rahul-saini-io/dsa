def run_len_encode(s):
    count = 1
    prev = s[0]
    res = ""

    for i in range(1, len(s)):
        if count==9 or prev != s[i]:
            res += str(count) + prev
            count = 1
            prev = s[i]
        else:
            count+=1

    # handle last combo
    res+= str(count) + prev

    return res


s = "AAAAAAAAAAAABBBBCCCDDDDDDDDDD"
print(run_len_encode(s))