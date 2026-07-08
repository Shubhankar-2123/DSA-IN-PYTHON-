n = 5378
num = n
result = 0 

while num > 0:
    ld = num%10
    result =  result * 10 + ld
    num = num// 10

if n == ld :
    print("Is a Palindrome.")
else: 
    print("Not a Palindrome")

    
    

