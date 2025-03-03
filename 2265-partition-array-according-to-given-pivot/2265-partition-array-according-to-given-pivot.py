class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = []

        count = 0

        for n in nums:
            if n < pivot:
                arr.append(n)
            elif n == pivot:
                count += 1
        
        while count != 0:
            arr.append(pivot)
            count -= 1
        
        for n in nums:
            if n > pivot:
                arr.append(n)
        
        return arr
        