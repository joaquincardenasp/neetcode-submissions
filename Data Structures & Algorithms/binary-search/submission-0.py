class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            k = (left + right) // 2
            if target < nums[k]:
                right = k-1
            elif target > nums[k]:
                left = k+1
            elif target == nums[k]:
                return k
        return -1