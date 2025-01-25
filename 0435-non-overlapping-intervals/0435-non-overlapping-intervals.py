class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort intervals
        intervals.sort(key = lambda i:i[0])
        count = 0

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)
        
        return count


        