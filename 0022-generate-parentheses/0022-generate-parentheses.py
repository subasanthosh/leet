class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def rec(n,ans,s="",open=0,close=0):
            
            if len(s)==2*n:
                ans.append(s)
                return

            if open < n:
                rec(n,ans,s+'(',open+1,close)

            if close < open:
                rec(n,ans,s+')',open,close+1)
        ans = []
        rec(n,ans)
        
        return ans
                