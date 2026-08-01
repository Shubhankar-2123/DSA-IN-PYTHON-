nums = [3,5,6,8,9,10,20]

def Check_If_Sorted(nums):

    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
        
    return True


print(Check_If_Sorted(nums))

    