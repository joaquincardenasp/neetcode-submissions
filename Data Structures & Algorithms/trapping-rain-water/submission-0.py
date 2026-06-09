class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        total = 0
        while right > left:
            if height[left] < height[right]:
                max_left = max(height[left], max_left)
                total += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right], max_right)
                total += max_right - height[right]
                right -=1     
        return total