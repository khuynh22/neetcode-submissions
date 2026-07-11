class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtracking(index, curr_str):
            if len(digits) == len(curr_str):
                res.append(curr_str)
                return
            
            for char in key_map[digits[index]]:
                backtracking(index + 1, curr_str + char)
            
        
        if digits:
            backtracking(0, "")
        
        return res
