class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        i = 0
        while i < n:
            prefix = 0
            for j in range(i,n):
                prefix += nums[j]
                arr.append(prefix)
            i += 1
        arr.sort()
        return sum(arr[left-1:right]) % 1000000007