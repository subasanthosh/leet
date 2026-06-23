class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in s[::-1]:
            if i==' ' and c>=1:
                break
            if i==' ':
                continue
            c+=1
        return c

        