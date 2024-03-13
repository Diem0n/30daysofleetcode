class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float('-inf')
        
        p = 1
        for i in range(n):
            p *= nums[i]
            
            max_prod = max(p , max_prod)
            
            if (p == 0):
                p = 1
        p = 1
        for i in range(n-1 , -1 , -1):
            p *= nums[i]
            
            max_prod = max(p , max_prod)
            
            if (p == 0):
                p = 1
        return max_prod