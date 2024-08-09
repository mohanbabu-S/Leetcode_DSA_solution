class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        left,right,up,down = 0,n-1,0,n-1
        num=1
        while num<=(n**2):
            for x in range(left,right+1):
                res[up][x] = num
                num+=1
            up+=1

            for x in range(up,down+1):
                res[x][right] = num
                num+=1
            right-=1

            if left<=right:
                for x in range(right,left-1,-1):
                    res[down][x] = num
                    num+=1
                down-=1
            
            if up<=down:
                for x in range(down,up-1,-1):
                    res[x][left] = num
                    num+=1
                left+=1
            
        return res