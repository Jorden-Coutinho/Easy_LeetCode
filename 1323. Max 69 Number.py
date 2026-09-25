#method 1 - Integer Reversal and replacement
class Solution:
    def maximum69Number (self, num: int) -> int:
        rev = 0 
        num1 = num 
        c = False
        while num1 > 0:
            d = num1 % 10
            rev = rev * 10 + d
            num1 //= 10

        while rev > 0:
            d = rev%10
            print(d)
            if d == 6 and c == False:
                d = 9
                c = True
            num1 = num1*10+d
            rev //=10
        return num1

#method 2 - 
