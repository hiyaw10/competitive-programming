class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append((b,w))
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            currW, currNode = heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)
            t = max(t, currW)
            
            for n2, w2 in graph[currNode]:
                if n2 not in minHeap:
                    heappush(minHeap, (currW+w2, n2))
        return t if len(visited) == n else -1
        
