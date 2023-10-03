class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)
        def check(u, v, graph):       
            visited = set()  
            stack = [u]     

            while stack:
                node = stack.pop()  

                if node == v:
                    return True  

                if node not in visited:
                    visited.add(node)
                    if node in graph:
                        for neighbor in graph[node]:
                            stack.append(neighbor)
            return False
        res = []
        for pre, course in queries:
            res.append(check(pre, course, graph))
            
        return res
