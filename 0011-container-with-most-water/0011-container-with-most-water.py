class Solution:
    def maxArea(self, height: List[int]) -> int:
        last, right = 0, len(height) - 1
        expect_res = 0

        while last < right:
            expect_res = max(expect_res, min(height[last], height[right]) * (right - last))
            if height[last] < height[right]:
                last += 1
            elif height[right] <= height[last]:
                right -= 1
            
        return expect_res