class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/k)
            
            if total > h:
                l = k + 1
            else:
                r = k -1
                result = k
        
        return result
