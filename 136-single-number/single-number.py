class Solution(object):
    def singleNumber(self, nums):
        res={}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1

        for i in nums:
            if res[i]==1:
                return i
                
        

       
            


