class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        result = 0

        for _ in range(n):
            curr = -1
            for i in range(n):
                if not in_mst[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            in_mst[curr] = True
            result += min_dist[curr]

            x1, y1 = points[curr]

            for neighbor in range(n):
                if not in_mst[neighbor]:
                    x2, y2 = points[neighbor]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[neighbor]:
                        min_dist[neighbor] = dist

        return result
        