class Solution:
    def canJump(self, nums: List[int]) -> bool:
        req_goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= req_goal:
                req_goal = i
        return req_goal == 0