class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                val = -1 * (abs(first) - abs(second))
                heapq.heappush(stones, val)
        stones.append(0)
        return abs(stones[0])
        