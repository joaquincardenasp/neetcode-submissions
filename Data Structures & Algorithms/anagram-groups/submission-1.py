class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            letters = [0] * 26

            for letter in i:
                letters[ord(letter) - ord("a")] +=1

            groups[tuple(letters)].append(i)
        return list(groups.values())