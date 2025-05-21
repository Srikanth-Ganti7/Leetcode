class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()

        preMap = {i:[] for i in range(numCourses)}

        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        
        def dfs(cur):
            if cur in visit:
                return False
            
            if preMap[cur] == []:
                return True
            
            visit.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visit.remove(cur)
            preMap[cur] = []
            return True
        
        for cur, pre in prerequisites:
            if not dfs(cur):
                return False
        
        return True



        