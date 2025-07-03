class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[1])

        prevEnd = float("-inf")

        for interval in intervals:

            if interval[0] < prevEnd:
                count += 1
            
            else:
                prevEnd = interval[1]
        
        return count

        