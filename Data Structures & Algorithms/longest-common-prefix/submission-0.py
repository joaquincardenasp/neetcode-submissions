class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i< len(prefix) and i < len(s) and s[i] == prefix[i]:
                i+=1
            prefix = s[:i]
        return prefix