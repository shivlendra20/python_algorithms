
class Solution:
    def divide(self, dividend : int, divisor : int) -> int:
        sign = 1
        count = 0
        
        if dividend < 0 or divisor < 0:
            sign = -1
            
        if dividend < 0 and divisor < 0:
            sign = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= divisor:
            dividend = dividend - divisor
            count += 1
        
        if sign == -1:
            
            count = -count
            return count
        
        return count
        
        

result = Solution()
print(f'Division is {result.divide(7, -3)}')