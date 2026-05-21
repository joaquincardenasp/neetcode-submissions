class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicS = {}
        dicT = {}
        for char in range(len(s)):
            dicS[s[char]] = dicS.get(s[char], 0) + 1
            dicT[t[char]] = dicT.get(t[char], 0) + 1
        for char in dicS:
            if dicS[char] != dicT.get(char, 0):
                return False
        return True