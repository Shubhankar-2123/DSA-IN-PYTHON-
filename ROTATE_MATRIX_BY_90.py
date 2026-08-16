matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotate_matrix_90_bruteforce(matrix):
    n = len(matrix)
    
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = matrix[i][j] 
    

    print(result)
# rotate_matrix_90_bruteforce(matrix)

def rotate_matrix_90_optimal(matrix):
    n = len(matrix)

    for i in range(0,n-1):
        for j in range(i+1,n):
            matrix[i][j] ,matrix[j][i]= matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

rotate_matrix_90_optimal(matrix)
print(matrix)