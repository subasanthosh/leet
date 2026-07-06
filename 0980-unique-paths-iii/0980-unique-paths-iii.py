class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        def find(i,j,soln,grid,steps,size,m,n):
            nonlocal count
            if i<0 or j<0 or i>=m or j>=n or soln[i][j]==1 or grid[i][j]==-1:
                return False

            if grid[i][j]==2:
                #print("dest")
                if steps==size:
                    count+=1
                return

            soln[i][j]=1
            for mx,my in moves:
                if find(i+mx,j+my,soln,grid,steps+1,size,m,n):
                    return

            soln[i][j]=0

        size = 0
        start = [0,0]
    
        for i in range(len(grid)):
            n=0
            for j in range(len(grid[i])):
                n+=1
                if grid[i][j]==1:
                    start[0]=i
                    start[1]=j
                    size+=1
                elif grid[i][j]!=-1 and grid[i][j]!=2:
                    size+=1
        print(start,size,n)
        soln = [[0]*n for i in range(len(grid))]
        find(start[0],start[1],soln,grid,0,size,len(grid),n)
        return count
                    
