class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(s)
        l2 = len(p)
        s1arr = [0]*26
        s2arr = [0]*26
        ans = []
        if l<l2:
            return ans
        for i in p:
            s1arr[ord(i)-97] += 1

        #print(s1arr)

        for i in range(l2):
            s2arr[ord(s[i])-97]+=1


        for i in range(l-l2):
            if s1arr==s2arr:
                ans.append(i)
            s2arr[ord(s[i])-97] -= 1
            s2arr[ord(s[i+l2])-97] += 1
        if s1arr == s2arr:
            ans.append(l-l2)
        return ans