nums = [4,1,7,6,3,2,8]

def Partition_Array(nums ,low ,high):
    pivot=nums[low]
    i=low
    j=high
    while i < j :
        while nums[i]<=pivot and i <= high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j

def Quick_Sort(nums,low,high):

    if low<high:
        p_index = Partition_Array(nums ,low , high)
        Quick_Sort(nums,low,p_index-1)
        Quick_Sort(nums,p_index+1,high)


Quick_Sort(nums,0,len(nums)-1)
print(nums)