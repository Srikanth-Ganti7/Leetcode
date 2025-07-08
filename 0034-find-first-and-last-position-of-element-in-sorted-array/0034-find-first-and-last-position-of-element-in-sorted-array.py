class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstIndex(nums, target):
            res = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                
                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    res = mid
                    right = mid - 1

            return res

        def lastIndex(nums, target):
            res = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                
                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    res = mid
                    left = mid + 1
            
            return res

        first = firstIndex(nums, target)
        last = lastIndex(nums, target)

        return[first, last]
            



        