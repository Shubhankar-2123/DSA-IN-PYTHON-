nums = [3,1,2,4,1,5,2,6,4]


def Merge_Array(arr1,arr2):
    result = []
    i,j = 0,0
    n,m = len(arr1),len(arr2)

    while i<n and j<m:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    if i<n:
        while i<n:
            result.append(arr1[i])
            i+=1

    if j<m:
        while j<m:
            result.append(arr2[j])
            j+=1
    return result

def Merge_Sort(arr):
    if len(arr) <=1 :
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = Merge_Sort(left_arr)
    right = Merge_Sort(right_arr)

    return Merge_Array(left,right)
    

print(Merge_Sort(nums))
        
            
