# Reverse array using recursion

arr = [5,7,3,2,6,1,5,9]

left = 0
right = len(arr) - 1

def fun(arr , left , right):
    if left >=right:
        return
    arr[right],arr[left] = arr[left],arr[right]
    fun(arr, left+1,right-1)
    return arr

print(fun(arr,left,right))