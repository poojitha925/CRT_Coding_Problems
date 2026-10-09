class Solution:
    def countDigits(self, n: int) -> int:
        # Code here
      count=0
      digit=0
      if n==0:
          return 1
      while n>0:
          digit=n%10
          count+=1
          n=n//10
      return count 