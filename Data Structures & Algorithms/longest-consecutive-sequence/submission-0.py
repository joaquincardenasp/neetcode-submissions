class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has = set(nums)
        longest = 0
        for i in has:
            if i-1 not in has:
                start = i + 1
                while start in has:
                    start += 1
                longest = max(longest, start - i)
        return longest