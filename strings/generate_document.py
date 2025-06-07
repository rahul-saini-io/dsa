def generate_doc(chars, doc):
    """
        Check if we can use chars to make our document
        chars string can have duplicate chars which is not a problem
        we just have to make sure that chars in chars string adds up to make document string spaces, symbol included.

    """

    f_map = {}
    for ch in chars:
        if ch in f_map:
            f_map[ch] += 1
        else:
            f_map[ch] = 1

    for ch in doc:
        if ch not in f_map or f_map[ch] == 0:
            return False
        else:
            f_map[ch] -= 1
    return True




chars = "Bste!hetsi ogEAxpelrt x "
doc = "AlgoExpert is the Best!"

print(generate_doc(chars, doc))