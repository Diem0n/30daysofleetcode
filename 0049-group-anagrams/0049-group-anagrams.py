class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            if not s:
                anagram_groups[''].append('')
                continue
            char_count = [0] * 26
            for char in s:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)
            anagram_groups[key].append(s)
        return list(anagram_groups.values())