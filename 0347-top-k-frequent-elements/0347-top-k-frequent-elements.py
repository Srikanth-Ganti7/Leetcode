class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hmap = {}
        for n in nums:
            Hmap[n] = 1 + Hmap.get(n, 0)
        
        print(Hmap)

        Heap = []
        for key, value in Hmap.items():
            heapq.heappush(Heap, (value,key))
            if len(Heap)>k:
                heapq.heappop(Heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(Heap)[1])
        
        return res

        