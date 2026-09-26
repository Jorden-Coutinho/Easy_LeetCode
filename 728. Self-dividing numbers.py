class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        
        for num in range(left, right + 1):
            temp = num
            is_self_dividing = True
            
            while temp > 0:
                digit = temp % 10
                # Self-dividing numbers cannot contain '0' and must be divisible by all their digits
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
                temp //= 10  # Integer division to move to the next digit
            
            if is_self_dividing:
                result.append(num)
                
        return result
