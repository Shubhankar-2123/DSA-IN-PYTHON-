nums = [-2,1,-3,4,-1,2,1,-5,4]

def Max_Subarray_Sum(nums):
    n = len(nums)
    
  
    max = float("-inf")
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if max <= sum:
                max = sum
        

    return max



# print(Max_Subarray_Sum(nums))


# Kadane's Algorithm
def Max_Subarray_Sum_Optimal(nums):
    n =len(nums)
    max = float("-inf")
    total = 0
    for i in range(0,n):
        total += nums[i]
        if max < total:
            max = total
        if total < 0 :
            total = 0
    return max
      
print(Max_Subarray_Sum_Optimal(nums))
        
