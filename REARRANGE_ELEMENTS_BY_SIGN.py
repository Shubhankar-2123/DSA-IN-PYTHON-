nums = [5,10,-3,-1,-10,6]


def rearrange_by_sign_bruteforce(nums):
    n =len(nums)
    pos_index = []
    nev_index = []
    index = 0
    for num in nums:
        if num > 0:
            pos_index.append(num)
        else:
            nev_index.append(num)
    for i in range(0,n,2):
        nums[i] = pos_index[index]
        nums[i+1] = nev_index[index]
        index +=1
    return nums

# print(rearrange_by_sign_bruteforce(nums))


def rearrange_by_sign_optimal(nums):
    n = len(nums)
    result = [0] * n
    
    e_index = 0
    o_index = 1
    for i in range(n):
        
        if nums[i] >= 0:
            result[e_index]= nums[i]
            e_index+=2
        
        else:
            result[o_index] = nums[i]
            o_index+=2
        
    return result

print(rearrange_by_sign_optimal(nums))
