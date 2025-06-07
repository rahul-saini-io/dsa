def if_valid_subseq(a, b):
    b_idx = 0

    for val in a:
        if b[b_idx] == val:
            b_idx += 1
        if b_idx == len(b):
            # valid subsequence
            return True

    return False


a = [1,2,3,4,5,10]
b = [2,3,5]

print(if_valid_subseq(a, b))