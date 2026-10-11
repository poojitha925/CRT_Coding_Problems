class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n=len(nums)
        one_count=0
        ans=0
        for i in range(n):
            if nums[i]==1:
                one_count+=1
            ans=max(one_count,ans)
            if nums[i]==0:
                one_count=0
        return ans        
        