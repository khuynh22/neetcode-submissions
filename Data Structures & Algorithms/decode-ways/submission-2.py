class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp2 = 0
        temp = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                temp = 0
            else:
                temp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                temp += dp2
            
            temp, dp1, dp2 = 0, temp, dp1

        return dp1