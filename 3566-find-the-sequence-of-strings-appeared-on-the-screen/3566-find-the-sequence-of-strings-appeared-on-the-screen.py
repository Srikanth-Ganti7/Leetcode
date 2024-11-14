class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        strC = ""
        for c in target:
            
            strC+= "a"
            res.append(strC)

            while strC[-1] != c:

                strC = strC[:-1] + chr(ord(strC[-1]) + 1)
                res.append(strC)
        
        return res
                


        