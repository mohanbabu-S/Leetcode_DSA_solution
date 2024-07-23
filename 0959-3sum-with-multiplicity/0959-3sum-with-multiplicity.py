class Solution(object):
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        kMod = 10 ** 9 + 7
        res = 0
        count = Counter(arr)     # stores {num : freq}

        for x in count.keys():
            for y in count.keys():
                z = target - x - y

                # pass
                if z not in count:
                    continue

                # three of them have same values
                if x == y == z:
                    res += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    res = res % kMod

                # two of them have same values
                elif x == y != z:
                    res += count[x] * (count[x] - 1) // 2 * count[z]
                    res = res % kMod

                # x != y != z
                elif x < y < z:
                    res += count[x] * count[y] * count[z]
                    res = res % kMod

        return res % kMod