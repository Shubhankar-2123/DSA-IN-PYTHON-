nums = [55,32,97,-55,45,32,88,21,97]

def Second_Largest(nums):
    largest = float('-inf')
    sec_largest = float("-inf")

    for i in range(0,len(nums)):
        if largest < nums[i] :
            sec_largest = largest
            largest = nums[i]
        elif sec_largest < nums[i]and nums[i]!=largest:
            sec_largest = nums[i]
    return sec_largest

print(Second_Largest(nums))