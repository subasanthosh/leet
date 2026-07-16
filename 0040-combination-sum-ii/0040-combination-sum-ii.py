class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def find(i,cand,soln,tar,summ):

            if summ==tar:
                ans.append(soln.copy())
                return False

                
            if summ>tar:
                return False
                
        
            for j in range(i,len(cand)):
                if i<j and cand[j]==cand[j-1]:
                    continue

                soln.append(cand[j])

                find(j+1,cand,soln,tar,summ+cand[j])
                soln.pop()

        candidates.sort()

        find(0,candidates,[],target,0)
        return ans

