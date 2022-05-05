class Solution:
    from collections import deque
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_g = [[] for _ in range(len(graph))]
        outdeg = [0]*len(graph)
        q = deque([])
        for i in range(len(graph)):
            outdeg[i] = len(graph[i])
            if outdeg[i] == 0:
                q.append(i)
            for item in graph[i]:
                reverse_g[item].append(i)
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for neighbor in reverse_g[u]:
                outdeg[neighbor] -= 1
                if outdeg[neighbor] == 0:
                    q.append(neighbor)
        return sorted(res)
        
#Runtime: 723 ms, faster than 77.17% of Python3 online submissions for Find Eventual Safe States.
#Memory Usage: 21.7 MB, less than 65.70% of Python3 online submissions for Find Eventual Safe States.
