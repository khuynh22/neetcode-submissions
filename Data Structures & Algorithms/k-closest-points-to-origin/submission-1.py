class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        res = []

        for coor in points:
            x, y = coor[0], coor[1]
            heapq.heappush(max_heap, (-math.sqrt(x**2 + y **2), x, y))
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for _, x, y in max_heap:
            res.append([x, y])

        return res
        