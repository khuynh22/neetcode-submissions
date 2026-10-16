class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x = int(x / 10)

            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0
            if res < MIN_INT // 10 or (res == MIN_INT // 10 and digit < MIN_INT % 10):
                return 0

            res = (res * 10) + digit
        
        return res * sign