class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        
        heapq.heapify(maxHeap)

        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt,time + n])

            if q and time == q[0][1]:
                val = q.popleft()[0]
                heapq.heappush(maxHeap, val)
        return time
            


        