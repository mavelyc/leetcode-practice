import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        ins = collections.defaultdict(int)
        for e in prerequisites:
            graph[e[1]].append(e[0])
            ins[e[0]] += 1
        
        remaining_edges = len(prerequisites)
        stack = [x for x in range(numCourses) if ins[x] == 0]
        
        while stack:
            curr = stack.pop()
            
            for edge in graph[curr]:
                ins[edge]-=1
                remaining_edges-=1
                if ins[edge] == 0:
                    stack.append(edge)
        
        return remaining_edges == 0