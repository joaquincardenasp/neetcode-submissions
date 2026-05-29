class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            word_len = int(s[i:j])
            word = s[j+1 : j+1+word_len]
            i = j + 1 + word_len 
            decoded.append(word)
        return decoded