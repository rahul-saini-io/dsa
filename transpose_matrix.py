def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols) ]
    print(result)
    for i in range(rows):
        for j in range(cols):
            result[j][i]=matrix[i][j]
            print(result)


    # return result


matrix = [
    [1, 4],
    [2, 5],
    [3, 6]
]

"""
    output = [
        [1,2,3],
        [4,5,6]
    ]
"""

print(transpose(matrix))
