class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        # totalSum = sum(apple)
        # capacity.sort(reverse = True)
        # count = 0

        # for cap in capacity:
        #     totalSum -= cap
        #     count += 1
        #     if totalSum <=0:
        #         return count

        totalSum = sum(apple)
        maxHeap = [-c for c in capacity]
        heapq.heapify(maxHeap)

        boxes = 0

        while totalSum > 0 and maxHeap:
            totalSum += heapq.heappop(maxHeap)
            boxes += 1
        
        return boxes

        

        