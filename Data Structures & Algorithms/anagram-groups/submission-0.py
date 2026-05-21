class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []
        for i, n in enumerate(strs):
            sorted_word = "".join(sorted(n))
            if sorted_word not in groups:
                groups[sorted_word] = []
                groups[sorted_word].append(n)
            else:
                groups[sorted_word].append(n)
        return list(groups.values())