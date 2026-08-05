nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

def Merge_Array_My_Version(nums1 , nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    i , j = 0,0
    arr = []
    while i < n1 or j < n2:
        
        while i < n1 - 1 and nums1[i] == nums1[i+1]:
            i+=1
        
        while j < n2-1 and nums2[j] == nums2[j+1]:
            j+=1
        if i < n1 and j < n2 :
            if nums1[i] == nums2[j]:
                arr.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]< nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        elif i < n1:
            arr.append(nums1[i])
            i+=1
        else : 
            arr.append(nums2[j])
            j+=1

    return arr
# print(Merge_Array_My_Version(nums1,nums2))

def Merge_array_optimal(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    result = []
    i,j=0,0
    while i < n and j < m :
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        else :
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1
    while j < m:
        if len(result) == 0 or result[-1] != nums2[i]:
            result.append(nums2[j])
        j+=1
    return result

print(Merge_array_optimal(nums1,nums2))