class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_n = 0
        for n in range(0, len(nums) + 1):
            xor_n ^= n
        res = xor_n
        for n in nums:
            res = res ^ n
        
        return res