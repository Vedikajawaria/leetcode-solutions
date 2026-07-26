class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:1+i]
        return ""


        