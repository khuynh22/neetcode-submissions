class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        longest_window = 0
        left = 0

        for right in range(len(s)):
            count_map[s[right]] = 1 + count_map.get(s[right], 0)
            
            while (right - left + 1) - max(count_map.values()) > k:
                count_map[s[left]] -= 1
                left += 1
            longest_window = max(longest_window, right - left + 1)

        return longest_window
        