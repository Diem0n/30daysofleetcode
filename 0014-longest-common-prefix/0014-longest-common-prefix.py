class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        p = strs[0]  

        for s in strs[1:]:
            while p:
                if s.startswith(p):
                    break
                p = p[:-1]
            else:
                return ""

        return p