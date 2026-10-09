class Solution:
    def isPalindrome(self, x: int) -> bool:
       r=0
       original=x
       if original<0:
         return False
       while x!=0:
            digit=x%10
            r=r*10+digit
            x//=10
       if original==r:
        return True
       else:
        return False