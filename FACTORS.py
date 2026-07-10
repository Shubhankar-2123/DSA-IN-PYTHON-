from math import sqrt
n = 36
num = n 


# Brute Force
def BruteForce(num):
    result = []
    for i in range (1,num+1):
        if num % i == 0 :
            result.append(i)

    print(result)

def BetterSoln(num):
    result = []
    for i in range(1,(num //2) +1):
        if num % i == 0 :
            result.append(i)
    result.append(num)
    print(result)      

def OptimalSoln(num):
    result = []
    for i in range (1,int(sqrt(num))+1):
        if num % i == 0 :
            result.append(i)
            if num // i != i:
                result.append(num//i)
    # result.sort()
    print(result)
BruteForce(num)
BetterSoln(num)
OptimalSoln(num)