class Solution:
    @staticmethod
    def dac(strs, left, right):
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            prefix_left = Solution.dac(strs, left, mid)
            prefix_right = Solution.dac(strs, mid + 1, right)
            return Solution.common_prefix(prefix_left, prefix_right)
    @staticmethod
    def common_prefix(str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:min_len]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return Solution.dac(strs, 0, len(strs) - 1)

   