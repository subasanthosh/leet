class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        k = 1
        for i in nums:
            if i==k:
                k+=1
        return k