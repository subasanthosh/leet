class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fl = []
        for i in nums:
            if i in fl:
                fl.remove(i)
            else:
                fl.append(i)
        return fl[0] 

        