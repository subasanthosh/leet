class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums)):
            flag = 1
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    flag = 0
                    nums[j],nums[j+1] = nums[j+1],nums[j]
            if flag!=0:
                break