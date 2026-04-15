class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for num in range(n + 1):
            count = 0
            temp = num
            while temp > 0:
                if temp & 1 == 1:
                    count += 1
                temp >>= 1
            res[num] = count
        
        return res