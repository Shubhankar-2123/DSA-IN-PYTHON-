nums = [9,6,4,2,3,5,7,0,1]

def Missing_Number_Bruteforce(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i


# print(Missing_Number_Bruteforce(nums))
def Missing_Number_Better(nums):
    n = len(nums)
    frequency =  {i: 0 for i in range(n+1)}
    for i in range(n):
        frequency[nums[i]] += 1

    for missing_number , count in frequency.items():
        if count == 0 :
            return missing_number

print(Missing_Number_Better(nums))

def Missing_Number_Optimal(nums):
    n = len(nums)
    # sum1 = 0
    # sum2 = 0
    # for i in range(n):
    #     sum1 = sum1 + (i+1)
    #     sum2 = sum2 + nums[i]
    #     missingnumber = sum1 - sum2

    # return missingnumber

    return n(n+1)/2 - sum(nums)
# print(Missing_Number_Optimal(nums))
