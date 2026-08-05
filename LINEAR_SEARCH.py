nums = [5,3,9,8,1,6,4,-10,-100]
target  = 2
def Linear_Search(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i]==target:
            return i

    return -1

print(Linear_Search(nums,target))