class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])
        count = 1
        end = sorted_points[0][1]

        for s, e in sorted_points[1:]:
            if s<= end:
                continue
            else:
                count += 1
                end = e
            
        return count

with open("user.out", "w") as f:
    for points in map(loads, stdin):
        s = Solution()
        f.write(f"{s.findMinArrowShots(points)}\n")
exit(0)