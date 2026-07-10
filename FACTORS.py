n = 36
num = n 
result = []

# Brute Force
def BruteForce():
    for i in range (1,num+1):
        if num % i == 0 :
            result.append(i)

    print(result)

def BetterSoln():
    for i in range(1,(num //2) +1):
        if num % i == 0 :
                result.append(i)
    result.append(num)
    print(result)      

