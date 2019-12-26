import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        ins = collections.defaultdict(int)
        
        for edges in prerequisites:
            graph[edges[1]].append(edges[0])
            ins[edges[0]]+=1
            
        queue = [x for x in range(numCourses) if ins[x] == 0]
        final = []
        
        while queue:
            node = queue.pop(0)
            for nb in graph[node]:
                ins[nb]-=1
                if ins[nb] == 0:
                    queue.append(nb)
            final.append(node)
            
        return final if len(final) == numCourses else []
      