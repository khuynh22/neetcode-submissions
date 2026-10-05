class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = { 0 : 1 }
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum]  = 1 + prefix_sum.get(curr_sum, 0)
        
        return res