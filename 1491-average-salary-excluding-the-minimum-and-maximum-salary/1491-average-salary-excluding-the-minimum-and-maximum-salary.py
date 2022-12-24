class Solution:
    def average(self, salary: List[int]) -> float:
        List1 = []
        for i in salary:
            if i == max(salary) or i == min(salary):
                continue
            else:
                List1.append(i)
        return  sum(List1) / len(List1)       