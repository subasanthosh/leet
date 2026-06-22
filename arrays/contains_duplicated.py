class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for i in range(len(nums)):
            if nums[i] in l:
                return True
            l.add(nums[i])
        return False
        