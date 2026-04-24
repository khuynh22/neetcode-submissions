class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        while (i <= j):
            if (s[i].isalnum() and s[j].isalnum()) and (s[i].lower() != s[j].lower()):
                return False
            if not s[i].isalnum(): 
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            i += 1
            j -= 1

        return True