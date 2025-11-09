class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of array
        n = len(nums)
        answer = [1]*n
        # prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        # suffix product
        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
