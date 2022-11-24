class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Each letter represents attendance record
        A- absent
        L - late
        P - present
        The student can't skip for 2 or more classes(Total)
        The student can't be late for 3 or more consecutive days
        """
        count = 0
        for char in s:
            if char == "A":
                count += 1
        for char in s:
            if "LLL" in s or count >= 2:
                return False
        return True
            
            