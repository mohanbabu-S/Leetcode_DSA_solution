class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency = Counter(arr)
        for i in arr:
            if frequency[i] == 1 and k > 1:
                k -= 1
            elif frequency[i] == 1 and k == 1:
                return i

        return ""