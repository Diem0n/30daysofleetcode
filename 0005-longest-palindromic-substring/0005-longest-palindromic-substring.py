class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        processed_string = '#' + '#'.join(s) + '#'
        n = len(processed_string)
        p = [0] * n
        center = right = max_length = max_center = 0

        for i in range(n):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < n and processed_string[i - p[i] - 1] == processed_string[i + p[i] + 1]):
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
            if p[i] > max_length:
                max_length = p[i]
                max_center = i

        start = (max_center - max_length) // 2
        return s[start:start + max_length]