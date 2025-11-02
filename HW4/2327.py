class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for i in range(2, n + 1):
            start = i - delay
            end = i - forget
            if start >= 1:
                share += dp[start]
            if end >= 1:
                share -= dp[end]
            share %= MOD
            dp[i] = share
        
        return sum(dp[n - forget + 1 : n + 1]) % MOD
    
# Example 1:
# Input: n = 6, delay = 2, forget = 4
# Output: 5

# Example 2:
# Input: n = 4, delay = 1, forget = 3
# Output: 6

Sol = Solution()
print(Sol.peopleAwareOfSecret(6, 2, 4))  # 5
print(Sol.peopleAwareOfSecret(4, 1, 3))  # 6
