class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # helper function
        def atmost(goal):
            # guard condition 
            if goal < 0:
                return 0

            curr_sum = 0
            count = 0

            left = 0

            for right in range(len(nums)):
                curr_sum += nums[right]

                while curr_sum > goal:
                    curr_sum -= nums[left]
                    left += 1
                
                count += right - left + 1
            
            return count

        return atmost(goal) - atmost(goal-1)