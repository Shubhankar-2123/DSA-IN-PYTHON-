arr = [-1,0,1,2,-1,4]



def three_sum_bruteforce(arr):
    n = len(arr)
    my_set = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==0):
                    temp = [arr[i],arr[j],arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    return [list(ans) for ans in my_set]

print(three_sum_bruteforce(arr))
        
def three_sum_better(arr):
    result = set()
    for i in range(0,len(arr)):
        my_set = set()
        for j in range(i+1,len(arr)):
            third = -(arr[i]+arr[j])
            if third in my_set :
                temp = [arr[i],arr[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(arr[j])
    return  [list(ans) for ans in result]
print(three_sum_better(arr))
def three_sum_optimal(arr):
    ans = []
    arr.sort()
    for i in range(len(arr)):
        if i!=0 and arr[i]==arr[i-1]:
            continue

        j=i+1
        k=len(arr)-1

        while j<k:
            sum = arr[i]+arr[j]+arr[k]
            if sum < 0:
                j+=1
            elif sum>0:
                k-=1
            else:
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while j<k and arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+1]:
                    k-=1
    return ans
print(three_sum_optimal(arr))
