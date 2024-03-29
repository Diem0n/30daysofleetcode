class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        start = 0
        seen = set()

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            max_length = max(max_length, end - start + 1)
            seen.add(s[end])

            if max_length >= len(s) - start:
                break

        return max_length