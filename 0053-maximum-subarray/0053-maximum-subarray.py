class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        expect_res = nums[0]

        total = 0
        for n in nums:
            total += n
            expect_res = max(expect_res, total)
            if total < 0:
                total = 0
        return expect_res