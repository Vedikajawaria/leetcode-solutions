class Solution(object):
    def maxDepth(self, s):
        CURR_DEPTH=0
        MAX_dEPTH=0
        for ch in s:
            if ch=='(':
                CURR_DEPTH+=1
                MAX_dEPTH=max(MAX_dEPTH,CURR_DEPTH)
            elif ch==')':
                CURR_DEPTH-=1
        return MAX_dEPTH