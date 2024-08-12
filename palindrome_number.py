class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        
        reversed_x = 0
        original_x = x
        while x > 0:
            reversed_x = (reversed_x * 10) + (x % 10)
            x = x // 10
        
       
        if reversed_x == original_x:
            return True
        else:
            return False
