class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        summ = 0
        l = len(code)
        res = [0]*l

        if k>0:
            for i in range(1,k+1):
                summ += code[i]
            res[0] = summ

            for i in range(1,l):
                summ -= code[i]
                summ += code[(i+k)%l]
                res[i] = summ

        
        elif k<0:
            k = -k
            for i in range(l-k,l):
                summ += code[i]
            res[0] = summ
            for i in range(1,l):
                summ -= code[(i-k-1)%l]
                summ += code[i-1]
                res[i] = summ
        return res


            
