class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        x=(len(digits)) - 1
        if digits[x] == 9:
            digits[x] = 1
            digits.append(0)
            y = x
            while digits[y-1] == 9:
                digits[y-1] = 1
                digits[y] = 0
                y-=1 
        else:
            digits[x] = digits[x] + 1
        return digits
