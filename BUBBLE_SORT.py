

nums = [1,2,3,4,5,6,7,8]

def Bubble_Sort(nums):
    count = 0
    for i in range(0 , len(nums)-1):
        is_swap = False
        
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap = True
                print(nums)
            count +=1

        if is_swap == False:
            break
    print(nums)
    print(count)

    
Bubble_Sort(nums)