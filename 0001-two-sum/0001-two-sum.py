class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for idx, num in enumerate(nums):
            if num in dict:
                return dict[num],idx
            else:
                dict[target-num]=idx
        return [] 