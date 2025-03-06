class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0,0]

        hashMap = {}

        count = 0
        for a in grid:
            for b in a:
                hashMap[b] = hashMap.get(b,0) + 1
                count += 1
        
        print(hashMap)

        print(count)

        for num in range(1, count+1):
            if num in hashMap:
                if hashMap[num] == 2:
                    ans[0] = num
            else:
                ans[1] = num
        return ans

        