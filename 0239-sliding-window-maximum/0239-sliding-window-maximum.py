class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        expect_output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                expect_output.append(nums[q[0]])
                l += 1
            r += 1

        return expect_output