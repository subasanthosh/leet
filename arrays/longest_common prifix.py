class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=1
        ch = ''
        minn = len(strs[0])
        for i in strs:
            minn = min(minn,len(i))
        for i in range(minn):
            c=1
            for j in strs[1:]:
                if strs[0][i]==j[i]:
                    c+=1
            if c==len(strs):
                ch+=strs[0][i]
            else:
                break

        return ch

                   
        

        