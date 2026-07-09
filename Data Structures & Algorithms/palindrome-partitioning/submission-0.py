class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: list[list[str]] = []
        sub_list: list[str] = []
        
        def backtracking(start_index, end_index):
            if end_index >= len(s):
                if end_index == start_index:
                    res.append(sub_list.copy())
                return
            
            if s[start_index: end_index + 1] == s[start_index: end_index + 1][::-1]:
                sub_list.append(s[start_index: end_index + 1])
                backtracking(end_index + 1, end_index + 1)
                sub_list.pop()
            
            backtracking(start_index, end_index + 1)
        
        backtracking(0, 0)
        return res
