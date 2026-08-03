nums = [3,9,5,6,7,2,8]
k = 5


def K_Rotation_Bruteforce(nums,k):
    n = len(nums)
    for _ in range(0,k%n ):
        temp = nums[n-1]                # temp = nums.pop()
        for j in range(n-2,-1,-1):      # nums.insert(0,temp)
            nums[j+1] = nums[j]
        nums[0]= temp
    


def K_Rotation_Better(nums,k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]

def K_Rotation_Optimal(nums,k):
    n = len(nums)
    k = k%n

    def Reverse_Array(nums,left,right):
        while left < right :
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -=1
            print(nums)

    Reverse_Array(nums,0,n-1)
    Reverse_Array(nums,0,k-1)
    Reverse_Array(nums , k ,n-1)

K_Rotation_Optimal(nums,k)
print(nums)

    