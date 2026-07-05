class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(nums, index):
            if index == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtracking(nums, index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        
        backtracking(nums, 0)
        return res