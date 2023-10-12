class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for i, edge in enumerate(edges):
            
            a, b = edge
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        
        
        pq = [(-1, start_node)]
        
        visit = set()
        
        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)
            
            if cur == end_node:
                return prob * -1
            for nei, edgeProb in graph[cur]:
                if nei not in visit:
                    heappush(pq, (prob * edgeProb, nei))
        return 0
    
        
            
        
        
