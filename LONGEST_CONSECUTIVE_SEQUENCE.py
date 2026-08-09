nums =[1, 99, 101, 98, 2, 5, 3, 100,1,1]
def longest_sequence_bruteforce(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count +=1
            num +=1
        max_count = max(max_count,count)
    return max_count


def longest_sequence_better(nums):
    nums.sort()
    count = 0
    last_smaller = float("-inf")
    longest = 0
    for i in range(len(nums)):
        num = nums[i]
        if num - 1 == last_smaller:
            count +=1
            last_smaller = num
        elif num != last_smaller :
            count = 1
            last_smaller = num
        longest = max(longest,count)
    return longest

def longest_sequence_optimal(nums):
    my_set = set()
    for num in nums :
        my_set.add(num)
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count+=1
                x+=1
            longest = max(longest,count)
    return longest

print(longest_sequence_bruteforce(nums))
print(longest_sequence_better(nums))
print(longest_sequence_optimal(nums))
    
       


    
       