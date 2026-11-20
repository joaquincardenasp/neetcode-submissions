class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        n = len(s)
        max_freq = 0
        answer = 0
        for right in range(n):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
        return answer