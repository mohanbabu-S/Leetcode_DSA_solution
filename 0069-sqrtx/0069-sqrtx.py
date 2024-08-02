class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 4: return 1 if x else 0
        s, e, m = 1, x, -1
        while(s <= e):
            m = (s + e)//2
            if m*m == x:
                return m
            elif m*m > x:
                e = m - 1
            else:
                s = m + 1
        return m - 1 if m * m > x else m