class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        min_len = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                min_len = min(min_len, R - L + 1)
                total -= nums[L]
                L += 1
            
        return 0 if min_len == float("inf") else min_len