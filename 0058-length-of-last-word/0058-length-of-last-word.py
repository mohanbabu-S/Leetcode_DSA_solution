class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c