class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
        
        components = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                components += 1
        
        return components
