class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        
        # Feasibility check
        minC = complexity[0]
        for i in range(1, n):
            if complexity[i] <= minC:
                return 0
            minC = min(minC, complexity[i])
        
        # (n-1)! permutations
        ans = 1
        for x in range(1, n):
            ans = ans * x % MOD
        
        return ans
