class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l = 0
        
        # maxL = []

        # for r in range(l+k-1, len(nums)):
        #     maxN = float("-infinity")
        #     for c in nums[l:r+1]:
        #         if c > maxN:
        #             maxN = c
            
        #     maxL.append(maxN)
        #     l += 1
        # return maxL


        output = []
        q = collections.deque()

        l,r = 0,0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            
            r+=1
        return output


        