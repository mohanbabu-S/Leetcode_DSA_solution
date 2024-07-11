class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        expect_res = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                expect_res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                expect_res += rightMax - height[right]
        return expect_res