class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                maxArea = max(area,maxArea)
                left += 1
            else:
                area = height[right]*(right - left)
                maxArea = max(area, maxArea)
                right -= 1
        return maxArea

        