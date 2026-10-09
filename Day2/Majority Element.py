class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        dici={}
        for val in nums:
            if val not in dici:
                dici[val]=1
            else:
                dici[val]=dici[val]+1
        ans=-1
        temp=n//2
        for i in dici:
            val=dici[i]
            if val>temp:
                ans=i
                break
        return ans