nums = [1,1,1,2,3,4,4,7,9,9,9,10]

def Remove_Duplicates_Bruteforce(nums):
    n = len(nums)
    f_map = {}

    for i in range(0,n):
        if i not in f_map:
            f_map[nums[i]]=0

    j = 0 
    for k in f_map:
        nums[j]= k
        j+=1
    return j


def Remove_Duplicates_Optimal(nums):
    i,j=0,1
    while j<len(nums):
        if nums[i] != nums[j]:
            i+=1
            nums[i]=nums[j]
            
        j+=1
    return i+1
p = Remove_Duplicates_Optimal(nums)
print(p)
print(nums[:p])