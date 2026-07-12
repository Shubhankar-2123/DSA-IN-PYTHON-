n = [5,3,2,2,1,5,5,7,5,10]

m = [10,111,1,9,5,67,2]

def BruteForce(n,m):
    for num in n :
        count = 0
        for x in m :
            if x == num :
                count +=1
        print(f"{num} occurs {count} times")

BruteForce(n,m)

