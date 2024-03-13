class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            n = len(nums)
            nums.sort()
            for i in range(n+1):
                if i not in nums: 
                    return i 
            return 0