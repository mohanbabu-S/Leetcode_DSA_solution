
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direction vectors: right, down, left, up
        ans = [[0] * n for _ in range(n)] 
        x = y = cnt = num = 0  # Initialize starting position, direction counter, and number counter
        while num < n * n:  
            if ans[x][y] == 0: 
                num += 1
                ans[x][y] = num  
            dx = x + d[cnt][0]
            dy = y + d[cnt][1]
            if 0 <= dx < n and 0 <= dy < n and ans[dx][dy] == 0:  # Check if the next position is valid
                x, y = dx, dy  # Move to the next position
            else:
                cnt = (cnt + 1) % 4  # Change direction clockwise
        return ans