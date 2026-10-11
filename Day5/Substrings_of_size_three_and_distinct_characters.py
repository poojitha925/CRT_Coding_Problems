class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        dici={}
        l=0
        ans=0
        for r in range(n):
            if s[r] not in dici:
                dici[s[r]]=1
            else:
                dici[s[r]]+=1
            if r-l==3:
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    dici.pop(s[l])
                l+=1
            if len(dici)==3:
                ans+=1
        return ans