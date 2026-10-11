class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        l=0
        r=0
        temp=0
        max_avg=0
        ans=float('-inf')
        for r in range(n):
            temp+=nums[r]
            if r-l==k:
                temp-=nums[l]
                l+=1
            if r-l+1==k:
                max_avg=temp/k
                ans=max(max_avg,ans)
        return ans