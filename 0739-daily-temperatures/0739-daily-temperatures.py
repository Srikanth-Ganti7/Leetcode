class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Brute Force
        # res = []

        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res.append(j-i)
        #             break
        #         else:
        #             if j == len(temperatures) - 1:
        #                 res.append(0)
        
        # return res

        #Stack:

        res = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res 





        