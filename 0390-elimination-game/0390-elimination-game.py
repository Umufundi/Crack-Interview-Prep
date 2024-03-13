class Solution:
    def lastRemaining(self, n: int) -> int:
        left_to_right = True
        step_counter = 1
        last_remaining = n
        while n > 1:
            if n%2 == 1 or not left_to_right:
                last_remaining = last_remaining - step_counter
            
            n = int(n/2)
            left_to_right = not left_to_right
            step_counter *= 2
        
        return last_remaining