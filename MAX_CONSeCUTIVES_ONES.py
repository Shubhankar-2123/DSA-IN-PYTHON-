nums = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]

def Max_Consecutives(nums):
    n = len(nums)
    temp = 0
    count = 0
    for i in range(n):
        if nums[i]==1:
            temp += 1
        else:
            if temp > count:
                count = temp
            temp = 0

    if temp >count:
        count = temp

    return count 
print(Max_Consecutives(nums))