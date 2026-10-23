class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i in range(len(nums)):
            if i!=nums[i]:
                k &= nums[i]
        return k if k!=-1 else 0