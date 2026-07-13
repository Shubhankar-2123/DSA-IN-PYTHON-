
# print x , n times 
def func(x,n):
    if n == 0 :
        return
    print(x)
    func(x,n-1)

func(15 , 4)

# print 1 to n using head recursion
def num(i,n):
    if i > n :
        return 
    print(i)
    num(i+1,n)
num(1,10)

#print 1 to n using tail (Backtracking) recursion
def fun(n):
    if n == 0 :
        return 
    fun(n-1)
    print(n)
fun(10)