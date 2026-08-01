class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for e1, e2 in edges:
            graph[e1].add(e2)
            graph[e2].add(e1)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        component = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                component += 1
        
        return component
