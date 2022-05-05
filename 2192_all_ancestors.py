class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indeg = [0]*n
        res = [[] for i in range(n)]
        def DFS(graph, node):
            stack = [node]
            vis = set()
            vis.add(node)
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in vis:
                        stack.append(v)
                        vis.add(v)
            return list(vis)
        for item in edges:
            to = item[0]
            fr = item[1]
            graph[fr].append(to)
            indeg[fr] += 1
        leaf = [x for x in range(n) if indeg[x] == 0]
            if len(graph[i]) == 0:
                continue
            tra = []
            for item in graph[i]:
                if item not in leaf:
                    tra += DFS(graph, item)
                else:
                    tra.append(item)
            res[i] = sorted(list(set(tra)))
        return res
#Runtime: 1078 ms, faster than 61.85% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
#Memory Usage: 28.6 MB, less than 97.70% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
      
