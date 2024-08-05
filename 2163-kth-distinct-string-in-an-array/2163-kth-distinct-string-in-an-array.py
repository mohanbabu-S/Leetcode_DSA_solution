class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
         return next((s for i, s in enumerate((s for s, c in Counter(arr).items() if c == 1), 1) if i == k), '')