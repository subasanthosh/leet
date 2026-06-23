class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s = ""
        for i in words:
            if i==i[::-1]:
                s = i
                break
        return s