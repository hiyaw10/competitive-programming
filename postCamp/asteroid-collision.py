class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack.pop()
                if abs(top) == abs(asteroid):
                    break
                elif abs(top) > abs(asteroid):
                    # The top asteroid survives.
                    stack.append(top)
                    break
                else:
                    continue
            else:
                stack.append(asteroid)
        
        return stack