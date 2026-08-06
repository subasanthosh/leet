class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
            prod = 1

            for i in str(n):
                prod*=int(i)

            while prod%t!=0:
                n+=1
                prod = 1
                for i in str(n):
                    prod*=int(i)
                print(n)
            return n
        