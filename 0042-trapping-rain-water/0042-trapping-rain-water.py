class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        leftPointer = 0
        rightPointer = len(height) - 1

        res = 0

        leftMax = height[leftPointer]
        rightMax = height[rightPointer]

        while leftPointer < rightPointer:
            if leftMax < rightMax:
                leftPointer += 1
                leftMax = max(leftMax, height[leftPointer])
                res += leftMax - height[leftPointer]
            
            else:
                rightPointer -= 1
                rightMax = max(rightMax, height[rightPointer])
                res += rightMax - height[rightPointer]
        return res

             
        