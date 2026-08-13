class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            curr = nums[i]

            dp_max[i] = max(curr, curr * dp_max[i - 1], curr * dp_min[i - 1])
            dp_min[i] = min(curr, curr * dp_max[i - 1], curr * dp_min[i - 1])

            res = max(res, dp_max[i])
        
        return res
