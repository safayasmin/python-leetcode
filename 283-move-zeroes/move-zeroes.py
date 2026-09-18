class Solution(object):
    def moveZeroes(self, nums):
        res=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(nums[i])
        for i in range(len(nums) - len(res)):
            res.append(0)

        nums[:] = res
        
        