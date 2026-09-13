class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last_index = {}
        for i, char in enumerate(s):
            char_to_last_index[char] = i
        
        res = []
        size = end = 0

        for i, char in enumerate(s):
            size += 1
            end = max(end, char_to_last_index[char])
            if i == end:
                res.append(size)
                size = 0
        
        return res