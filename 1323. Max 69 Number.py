class Solution:
    def maximum69Number (self, num: int) -> int:
        rev = 0
        num1 = num
        num2 = 0
        c = False
        while num1 > 0:
            d = num1 % 10
            rev = rev * 10 + d
            num1 //= 10


        while rev > 0:
            d = rev%10
            print(d)
            if d == 6:
                if c == False:
                    d = 9
                    c = True
            num2 = num2*10+d
            rev //=10
        return num2
