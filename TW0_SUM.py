# Constrain
# 1. Use one element once
# 2. Only one Solution exists

nums = [5,9,1,2,4,15,6,3]
target = 13

def Two_Sum_Bruteforce(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target :
                return [i,j]



# print(Two_Sum_Bruteforce(nums,target))

def Two_Sum_Optimal(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(n):
        remaining = target - nums[i] 
        if remaining in hash_map :
            return [hash_map[remaining],i]
        hash_map[nums[i]] = i

# print(Two_Sum_Optimal(nums,target))