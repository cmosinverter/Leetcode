class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for i in range(numCourses)]
        indeg = [0]*numCourses
        
        for item in prerequisites:
            u = item[0]
            v = item[1]
            
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
                    
        return sum(indeg) == 0
        
