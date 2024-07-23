class Solution:
    def minDistance(self, A, K):
        A.sort()
        N = len(A)
        P = [0] + list(accumulate(A))
        dp = [0] + [float('inf')] * N
        for i in range(K):
            for j in range(N - 1, i - 1, -1):
                for k in range(j, i - 1, -1):
                    m = (k + j) >> 1
                    cost = P[j + 1] + P[k] - 2 * P[m] - A[m] * (j - 2 * m + k + 1)
                    dp[j + 1] = min(dp[j + 1], dp[k] + cost)
        return dp[-1]