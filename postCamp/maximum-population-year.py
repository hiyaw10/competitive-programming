class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
       
        logs_dict = {}

        for n in logs:
            for i in range(n[0], n[1]):
                logs_dict[i] = logs_dict.get(i, 0) + 1

        sorted_logs = sorted(logs_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        most_frequent = sorted_logs[0][0]

        return most_frequent