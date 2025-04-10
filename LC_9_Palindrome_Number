class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if x<0:
            return False
        while(x>0):
           div = x%10
           rev = rev*10 + div
           x = x//10
        if temp == rev:
            return True

