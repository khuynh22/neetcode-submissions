class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # (i, t)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_ind, stack_t = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append((i, t))
        
        return res