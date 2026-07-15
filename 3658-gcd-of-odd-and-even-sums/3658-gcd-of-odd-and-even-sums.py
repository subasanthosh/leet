class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a = 0
        b = 0
        for i in range(1,(n*2)+1,2):
            a += i
            b += i+1

        while b:
            a,b = b,a%b

        return a
