class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = 0
        maxx = 0
        
        for i in range(k):
            if s[i] in "aeiou":
                count+=1
        maxx = max(maxx,count)
        if len(s)==1:
            return count
        for i in range(len(s)-k):
            if s[i] in "aeiou":
                count-=1

            if s[i+k] in "aeiou":
                count+=1

            maxx = max(maxx,count)
        return maxx
