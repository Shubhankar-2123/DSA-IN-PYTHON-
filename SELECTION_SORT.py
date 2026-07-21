nums = [5,7,8,4,1,6,9,2]

def Selection_Sort_Ascending(nums):
    for i in range (0 , len(nums)):
        min = i
        for j in range (i+1 , len(nums)):
            if nums[min] > nums[j]:
                min = j

        nums[i],nums[min]= nums[min], nums[i]

    print(nums)

def Selection_Sort_descending(nums):
    for i in range (0 , len(nums)):
        max = i
        for j in range (i+1 , len(nums)):
            if nums[max] < nums[j]:
                max = j
    
        nums[i],nums[max]= nums[max], nums[i]
    
    print(nums)

Selection_Sort_Ascending(nums)
Selection_Sort_descending(nums)











                