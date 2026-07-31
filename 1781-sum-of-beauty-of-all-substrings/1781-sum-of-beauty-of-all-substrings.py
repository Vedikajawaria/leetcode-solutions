class Solution(object):
    def beautySum(self, s):
        ans=0
        n=len(s)
        for i in range(n):
            f={}
            for j in range(i,n):
                f[s[j]]=f.get(s[j],0)+1
                maxi=max(f.values())
                mini=min(f.values())
                ans+=maxi-mini
        return ans
    


        