class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]
        indeg = [0]*numCourses
        ancestors = [set() for _ in range(numCourses)]
        for item in prerequisites:
            fr = item[0]
            to = item[1]
            graph[fr].append(to)
            ancestors[to].add(fr)
            indeg[to] += 1
            
        q = deque([x for x in range(numCourses) if indeg[x] == 0])
        
        while q:
            parent = q.popleft()
            for child in graph[parent]:
                ancestors[child].update(ancestors[parent])
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)
        res = [None]*len(queries)       
        for i in range(len(queries)):
            u = queries[i][0]
            v = queries[i][1]
            if u in ancestors[v]:
                res[i] = True
            else:
                res[i] = False
        return res
#Runtime: 749 ms, faster than 94.81% of Python3 online submissions for Course Schedule IV.
#Memory Usage: 17.5 MB, less than 95.52% of Python3 online submissions for Course Schedule IV.
