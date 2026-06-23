class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        i=0
        while i<len(nums):
            c=0
            if nums[i]==1:
                while(i<len(nums) and nums[i]!=0):
                    c+=1
                    i+=1
                maxx = max(maxx,c)
            i+=1
        return maxx

                

        