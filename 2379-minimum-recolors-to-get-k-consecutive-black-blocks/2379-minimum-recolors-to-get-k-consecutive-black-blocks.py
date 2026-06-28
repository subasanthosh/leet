class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        count = 0
        minn = float('inf')
        for i in range(k):
            if blocks[i]=="W":
                count += 1
        minn = count
        for i in range(len(blocks)-k):
            if blocks[i]=="W":
                count-=1
            if blocks[i+k]=="W":
                count+=1

            minn = min(minn,count)
       
        return minn
            

        

