from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        


        n = len(nums)
        res = [0] * n
    # Group indices by value
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)
    
        for val in groups:
            indices = groups[val]
            m = len(indices)
        
            total_sum = sum(indices)
            prefix_sum = 0
        
            for j, idx in enumerate(indices):
            # Left side: (count of elements to left * current index) - (sum of left indices)
                left_part = j * idx - prefix_sum
            
            # Right side: (sum of right indices) - (count of elements to right * current index)
                right_sum = total_sum - prefix_sum - idx
                right_part = right_sum - (m - 1 - j) * idx
            
                res[idx] = left_part + right_part
                prefix_sum += idx
            
        return res