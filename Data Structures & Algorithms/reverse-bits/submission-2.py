class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(32):
            bit = (n >> i) & 1
            m += (bit << (31 - i))
        return m