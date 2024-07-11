class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        expect_res = [1] * (len(nums))

        for i in range(1, len(nums)):
            expect_res[i] = expect_res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            expect_res[i] *= postfix
            postfix *= nums[i]
        return expect_res