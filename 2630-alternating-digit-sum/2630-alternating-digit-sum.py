class Solution:
    def alternateDigitSum(self, n: int) -> int:
        size = 0
        sum_odd = 0
        sum_even = 0
        flag = True

        while n > 0:
            rem = n % 10
            if flag:
                sum_odd += rem
                sum_even -= rem
            else:
                sum_odd -= rem
                sum_even += rem

            flag = not flag
            size += 1
            n //= 10

        if size % 2 == 1:
            return sum_odd

        return sum_even