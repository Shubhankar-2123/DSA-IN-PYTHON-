n = 153

num = n
sum = 0
nod = len(str(n))
while num > 0 :
    ld = num % 10
    sum = sum + ld**nod
    num = num // 10

if n == sum :
    print("Is a Armstrong.")
else:
    print("Not a Armstrong.")