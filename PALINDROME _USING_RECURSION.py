s = "abca"
left = 0
right = len(s)-1
def palindrome(s,left ,right):
    if left < right :
        if s[left] == s[right]:
            return palindrome(s,left+1,right-1)
        else:
            return False
    else:
        return True

  
print(palindrome(s,left,right))
result = palindrome(s,left,right)
if result == True:
    print("Is a palindrome")
else:
    print("not a palindrome")