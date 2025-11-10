class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window approach
        # length of array
        n = len(nums)
        # clac late initial window_sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        # slide the window
        for i in range(k,n):
            # subtraxct the number leaving 
            window_sum -= nums[i-k]
            # add the number entering
            window_sum += nums[i]
            # update the max
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum/k
