class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        s = list(s)
        while(i<len(s) and j>=0 and i<j):
            if (s[i] in "aeiou" or s[i] in "AEIOU"):
                if s[j] in "aeiou" or s[j] in "AEIOU":
                    s[i],s[j] = s[j],s[i]
                    i+=1
                    j-=1
                    continue 
            if s[i] not in "aeiou" and s[i] not in "AEIOU":
                print(s[i])
                i+=1
            if s[j] not in "aeiou" and s[j] not in "AEIOU":
                j-=1

        st = ''
        for i in s:
            st+=i
        return st

            


        