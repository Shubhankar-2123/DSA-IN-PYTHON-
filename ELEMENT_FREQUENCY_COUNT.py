n = [5,3,2,2,1,5,5,7,5,10]

m = [10,111,1,9,5,67,2]

def BruteForce(n,m):
    for num in n :
        count = 0
        for x in m :
            if x == num :
                count +=1
        print(f"{num} occurs {count} times")



def Optimal(n,m):
    hash_map = [0] * 11
    for num in n :
        hash_map[num] += 1

    for x in m :
        if x < 1 or x >10:
            print(f"{x} occurs 0 times")
        else :
            print(f"{x} occurs {hash_map[x]} times")

def Using_Dict(n,m):
    freq_count = {}
    for num in n:
        if num not in freq_count:
            freq_count[num] = 1
        else :
            freq_count[num] += 1

    for x in m :
        if x in freq_count:
            print(f'{x} occurs {freq_count[x]} times')
        else :
            print(f"{x} occurs 0 times")

Using_Dict(n,m)