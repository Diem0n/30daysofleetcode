class Solution(object):
    def singleNumber(self, nums):
       return reduce(operator.xor , nums)
