matrix = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

def setZerosBruteforce(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                for x in range( cols) :
                    if matrix[i][x] != 0:
                        matrix[i][x] = float('inf')
                for x in range (rows):

                    if matrix[x][j] != 0:
                        matrix[x][j] = float('inf')
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = 0
    print(matrix)

# setZerosBruteforce(matrix)


def setZerosOptimal(matrix):
    r = len(matrix)
    c = len(matrix[0])

    row = [0] * r
    col = [0] * c


    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(r):
        for j in range(c):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    print(matrix)

setZerosOptimal(matrix)