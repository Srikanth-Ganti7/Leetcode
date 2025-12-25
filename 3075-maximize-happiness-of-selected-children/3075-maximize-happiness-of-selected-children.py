class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse = True)

        # maxHeap = [-n for n in happiness]
        # heapq.heapify(maxHeap)
        
        total = 0
        
        for i in range(k):
            if i >= len(happiness):
                break
            
            gain = happiness[i] - i

            if gain <= 0:
                break
            
            total += gain
        
        return total




        