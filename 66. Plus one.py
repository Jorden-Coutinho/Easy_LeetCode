class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        x = [int(c) for c in str(num)]
        return x
