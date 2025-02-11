class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for t in range(len(edges)+1)]
        
        def dfs(node,prev):
            visit.add(node)
            for nei in adj[node]:
                if nei in visit and nei != prev:
                    return True
                
                if nei not in visit:
                    if dfs(nei, node):
                        return True
            return False
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
            visit = set()

            if dfs(u,-1):
                return [u,v]
        
        return []



        
                



        