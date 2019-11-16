import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapaz = [0 for _ in range(26)]
        
        for c in tasks:
            mapaz[ord(c)-ord('A')]+=1
            
        queue = list(filter(lambda x: x>0, mapaz))
        heapq._heapify_max(queue)
        
        time = 0
        while queue:
            i = 0
            tmp = []
            while i <= n:
                if queue:
                    if queue[0] > 1:
                        tmp.append(heapq._heappop_max(queue)-1)
                    else:
                        heapq._heappop_max(queue)
                time+=1
                if(not queue and len(tmp) == 0):
                    break
                i+=1
            for i in tmp:
                heapq.heappush(queue, i)
        return time