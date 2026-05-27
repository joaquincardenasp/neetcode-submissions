class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_frequent = {}
        for i in nums:
            if i not in k_frequent.keys():
                k_frequent[i] = 0
            k_frequent[i]+=1
        k_most = sorted(k_frequent, key=lambda x: k_frequent[x], reverse=True)
        return k_most[:k]
        