"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graphs = {}
        
        for employee in employees:
            graphs[employee.id] = employee
            
        def dfs(node):
            if not node.subordinates:
                return node.importance
            
            total = 0
            for subordinate in node.subordinates:
                total += dfs(graphs[subordinate])
            return total + node.importance
        return dfs(graphs[id])
        
                