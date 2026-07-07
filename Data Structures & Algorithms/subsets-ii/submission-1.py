class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        nums.sort()

        def backtracking(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtracking(index + 1, subset)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtracking(index + 1, subset)
        backtracking(0, [])
        return res
