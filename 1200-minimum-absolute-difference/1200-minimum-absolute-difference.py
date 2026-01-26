class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        res = []
        minVal =  float("inf")
        for i in range(len(arr)-1):
            value = arr[i+1] - arr[i]
            if value < minVal:
                res = []
                res.append([arr[i], arr[i+1]])
                minVal = value
            
            elif value == minVal:
                res.append([arr[i], arr[i+1]])
        
        return res

