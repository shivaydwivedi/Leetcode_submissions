from collections import deque

class Solution:
    def countPartitions(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)

        dp = [0] * n
        prefix = [0] * n
        
        maxQ = deque()
        minQ = deque()
        
        L = 0
        
        for i in range(n):
            x = nums[i]
            
            # push into maxQ (monotonic decreasing)
            while maxQ and maxQ[-1] < x:
                maxQ.pop()
            maxQ.append(x)
            
            # push into minQ (monotonic increasing)
            while minQ and minQ[-1] > x:
                minQ.pop()
            minQ.append(x)
            
            # shrink window until valid
            while maxQ[0] - minQ[0] > k:
                if nums[L] == maxQ[0]:
                    maxQ.popleft()
                if nums[L] == minQ[0]:
                    minQ.popleft()
                L += 1
            
            # dp calculation
            if L == 0:
                dp[i] = prefix[i-1] + 1 if i > 0 else 1
            else:
                dp[i] = (prefix[i-1] - prefix[L-2]) % mod if L >= 2 else prefix[i-1] % mod
            
            prefix[i] = (prefix[i-1] + dp[i]) % mod
        
        return dp[-1] % mod
