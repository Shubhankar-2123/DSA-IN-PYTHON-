matrix = [[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]

def sprial_order_mat(mat):

    if not mat or not mat[0]:
        return []

    result = []
    
    left  = top = 0
    bottom = right =len(mat)-1
    while top<= bottom and left <=right :
        for j in range(left,right+1):
            result.append(mat[top][j])
        top+=1
        
        for j in range(top,bottom+1):
            result.append(mat[j][right])
        right-=1

        if top <= bottom :

            for j in range(right ,left-1,-1):
                result.append(mat[bottom][j])
            bottom -=1

        if left <= right :
            for j in range(bottom ,top-1,-1):
                result.append(mat[j][left])
            left +=1
    return result

print(sprial_order_mat(matrix))
