nums = [4, 5, 0, 0, 0, 1, 0, 2]

def Move_Zeros_Myversion(nums):
    n = len(nums)
    i,j=0,1
    while i < n and j < n :
        if nums[i] == 0 and nums[j] != 0:
            nums[i],nums[j]= nums[j],nums[i]
            i+=1
            j+=1
           
        elif nums[i]!=0:
            i+=1
            j+=1
            
        else :
            j+=1

    print(nums)


def Move_Zeros_Optimal(nums):
    n = len(nums)

    i = 0 
    while i < n:
        if nums[i] ==0:
            break
        i+=1
    j = i=1
    while j < n:
        if nums[j] != 0 :
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1

    print(nums)
    
            
Move_Zeros_Myversion(nums)



