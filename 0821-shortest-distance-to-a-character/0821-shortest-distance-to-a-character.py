class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = list(s)
        a = []
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
                
        for i in range(len(s)):
            minn = len(s)
            for j in a:
                print(j,i)
                if abs(j-i) < minn:
                    minn = abs(j-i)

            s[i] = minn
        return s