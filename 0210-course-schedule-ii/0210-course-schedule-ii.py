class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReq = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        output = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in visit:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)

            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output

        