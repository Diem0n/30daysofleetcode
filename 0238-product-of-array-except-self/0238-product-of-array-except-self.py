
class Solution(object):
    def productExceptSelf(self, nums):
        s = len(nums)
        l = 1
        r = 1
        a = [1]*s
        n = len(nums)
        for i in range(s):
            a[i] *= l
            l *= nums[i]

        for j in range(n-1 , -1 , -1):
            a[j] *= r
            r *= nums[j]
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        