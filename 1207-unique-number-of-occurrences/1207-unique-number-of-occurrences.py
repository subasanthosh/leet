class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        s = set()
        for i in arr:

            d[i] = d.get(i,0)+1

        for k,i in d.items():
            s.add(i)

        return len(s)==len(d)
