class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d= set(nums)
        if len(nums) == len(d):
            return False
        else:
            return True