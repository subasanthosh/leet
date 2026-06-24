class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        l2 = len(s2)
        s1arr = [0]*26
        s2arr = [0]*26
        if l>l2:
            return False
        for i in s1:
            s1arr[ord(i)-97]+=1

        for i in range(l):
            s2arr[ord(s2[i])-97]+=1

        for i in range(l2-l):
            if s1arr==s2arr:
                return True
            s2arr[ord(s2[i])-97]-=1
            s2arr[ord(s2[i+l])-97] += 1
    
        
        return s2arr==s1arr

            
            