class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        p = 1  
        q = 1  

        for i in range(2, n + 1):
            current = p + q
            q = p
            p = current

        return p