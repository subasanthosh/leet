class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s = list(s)
        while i<j:
            if s[i].isupper():
                s[i]=chr(ord(s[i])+32)
            if s[j].isupper():
                s[j]=chr(ord(s[j])+32)
            print(s[i],s[j])
            if s[i].isdigit() or s[i].isalpha():
                if s[j].isdigit() or s[j].isalpha():
                    if s[i]==s[j]:
                        i+=1
                        j-=1
                    else:
                        j=len(s)
                        break
                else:
                    j-=1
                    continue
            else:
                i+=1
        
        return j!=len(s) or len(s)==1
                
        