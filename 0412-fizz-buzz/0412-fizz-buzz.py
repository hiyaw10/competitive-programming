class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
    
        for num in range(1, n+1):
            if num % 5 == 0 and num % 3 == 0:
                output.append("FizzBuzz")
            elif num % 3 == 0:
                output.append("Fizz")
            elif num % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(num))
    
        return output