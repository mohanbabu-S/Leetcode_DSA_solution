class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[longest])
                longest += 1
            charSet.add(s[r])
            res = max(res, r - longest + 1)
        return res