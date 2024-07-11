class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        k_freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)
        for n, c in num_count.items():
            k_freq[c].append(n)

        expe_res = []
        for i in range(len(k_freq) - 1, 0, -1):
            for n in k_freq[i]:
                expe_res.append(n)
                if len(expe_res) == k:
                    return expe_res