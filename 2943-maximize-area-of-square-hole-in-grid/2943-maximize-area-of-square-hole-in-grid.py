class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        hBars.sort()
        vBars.sort()
        

        def longestCon(arr):
            if not arr:
                return 0
            cnt = 1
            maxCnt = 0

            for i in range(len(arr) - 1):
                if arr[i+1] - arr[i] == 1:
                    cnt += 1
                
                else:
                    maxCnt = max(maxCnt, cnt)
                    cnt = 1
            
            return max(maxCnt, cnt)
        
        hMax = longestCon(hBars) + 1
        vMax = longestCon(vBars) + 1

        side = min(hMax, vMax)
        return side*side
