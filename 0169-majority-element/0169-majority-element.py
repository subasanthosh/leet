class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        max_=0
        max_e=nums[0]
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                if c>max_:
                    max_=c
                    max_e = nums[i]
                c=1
            else:
                c+=1
        if c >max_ and len(nums)!=1:
            max_=c
            max_e = nums[i]
        return max_e

