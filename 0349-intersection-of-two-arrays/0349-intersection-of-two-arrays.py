class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1<n2:
            nums1,nums2 = nums2,nums1
            n1,n2 = n2,n1
        a = []
        i = 0
        j = 0
        while i<n1 and j<n2:
            if nums1[i]==nums2[j]:
                if nums1[i] not in a:
                    a.append(nums1[i])
                i=0
                j+=1
            else:
                i+=1

            if i==n1:
                i=0
                j+=1

        return a
