def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def sum_list_recursive(arr):
    if not arr:
        return 0
    return arr[0] + sum_list_recursive(arr[1:])


def reverse_string_recursive(s):
    if s == "":
        return ""
    return reverse_string_recursive(s[1:]) + s[0]


if __name__ == "__main__":
    print("factorial_recursive(5)", factorial_recursive(5))
    print("fibonacci_recursive(6)", fibonacci_recursive(6))
    print("fibonacci_memo(30)", fibonacci_memo(30))
    print("sum_list_recursive([1,2,3,4])", sum_list_recursive([1, 2, 3, 4]))
    print("reverse_string_recursive('hello')", reverse_string_recursive('hello'))
# Basic Fundamentals
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