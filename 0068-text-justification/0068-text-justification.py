class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        curr, count, width = [], 0, 0

        for word in words:
            if width + len(word) + count > maxWidth:
                spaces = maxWidth - width
                temp = []
                for i, c in enumerate(curr):
                    temp.append(c)
                    if i != count - 1:
                        temp.append(" " * ceil(spaces / (count - i - 1)))
                        spaces -= ceil(spaces / (count - i - 1))
                temp.append(" " * spaces)
                output.append("".join(temp))
                curr, count, width = [], 0, 0

            curr.append(word)
            count += 1
            width += len(word)

        return output + [" ".join(curr).ljust(maxWidth)]