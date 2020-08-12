# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix):
    col_track = 0
    col_list = list()

    for row in matrix:
        for col in row:
            if col == 0:
                col_list.append(col_track)
            if col_track == len(row) - 1:
                col_track = 0
            else:
                col_track += 1

    for row_count, row in enumerate(matrix):
        for n in row:
            if n == 0:
                zero_add = []
                for i in range(len(row)):
                    zero_add.append(0)
                matrix[row_count] = zero_add

    while len(col_list) != 0:
        for row in matrix:
            row[col_list[0]] = 0
        col_list.pop(0)

if __name__ == '__main__':
    print( set_zeroes([
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ] ))

    print( set_zeroes([
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ] ))