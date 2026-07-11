nums = [5,6,7,7,1,9,111,1,1,5,1,1]

# Method 1 
def Method_1(nums):
    freq_map = {}
    for i in range (0,len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else :
            freq_map[nums[i]] = 1
   
    print(freq_map)
Method_1(nums)

def Method_2(nums):
    hash_map = {}
    for i in range (0 , len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

    print(hash_map)
Method_2(nums)