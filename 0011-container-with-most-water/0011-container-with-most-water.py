class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxx = 0
        while i<j:
            if height[i]<=height[j]:
                maxx = max(maxx,(j-i)*height[i])
                i+=1
            else:
                maxx = max(maxx,(j-i)*height[j])
                j-=1
            
        return maxx
       

        