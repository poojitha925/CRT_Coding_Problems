class Solution:
    def maxVowels(self, s: str, k: int) -> int:
         a="aeiou"
         l=0
         n=len(s)
         ans=0
         count=0
         for r in range(n):
            if s[r] in a:
                count+=1
            if r-l==k:
                if s[l] in a:
                    count-=1
                l+=1
            ans=max(ans,count)
         return ans
                   
         