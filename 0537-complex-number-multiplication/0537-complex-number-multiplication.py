class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #put both in a tuple
        a1, b1 = num = num1.split("+")
        a2, b2 = numII = num2.split("+")
        
        new = b1[0 : len(b1) -1]
        new2 = b2[0 : len(b2) -1]
        print(new2)
        x = int(a1) * int(a2)
        y = int(a1) * int(new2)
        z = int(new) * int(a2)
        a = int(new2) * int(new)
        X = str(x - a)
        Y = str(z + y)
        return X + "+" + Y + "i"