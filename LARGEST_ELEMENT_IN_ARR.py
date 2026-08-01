nums = [55,32,-97,99,3,67]


def Largest_Element(nums):
    largest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest:
            largest = nums[i]
    return largest

print(Largest_Element(nums))

