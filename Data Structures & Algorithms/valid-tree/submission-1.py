class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        graph = defaultdict(set)

        for e1, e2 in edges:
            graph[e1].add(e2)
            graph[e2].add(e1)
        
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visit) == n
