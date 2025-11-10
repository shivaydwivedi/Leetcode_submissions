class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        
        # We use a stack to maintain a non-decreasing sequence of “levels” seen so far.
        # We push a sentinel value 0 so the logic is simpler (all nums are >= 0).
        stack = [0]
        
        for num in nums:
            # While the current number is **less** than the stack’s top,
            # we pop because those “higher” segments cannot extend through this num.
            while stack and stack[-1] > num:
                stack.pop()
            
            # Now either stack is empty or stack[-1] ≤ num.
            # If stack is empty (should not happen if sentinel) or
            # the top is strictly < num, then we found a new “rise” to num.
            if not stack or stack[-1] < num:
                ans += 1
                stack.append(num)
            # If stack[-1] == num then we do nothing — same level continues.
        
        return ans