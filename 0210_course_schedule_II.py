class Solution:
    from collections import deque
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        res = []
        
        for item in prerequisites:
            u = item[0]
            v = item[1]
            graph[v].append(u)
            indeg[u] += 1
            
        q = deque([x for x in range(numCourses) if indeg[x] == 0])
        
        while q:
            u = q.popleft()
            res.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return res if sum(indeg) == 0 else []
      
#Runtime: 108 ms, faster than 79.39% of Python3 online submissions for Course Schedule II.
#Memory Usage: 15.4 MB, less than 97.33% of Python3 online submissions for Course Schedule II.
