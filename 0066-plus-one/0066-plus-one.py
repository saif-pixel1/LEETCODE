class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = len(digits)-1
                
    
        while l>=0:
            if digits[l] != 9:
                digits[l] = 1 + digits[l]
                return digits
            else:
                digits[l] = 0
                l-=1
        digits.insert(0,1)
        return digits
                


            
            
            
            
            






