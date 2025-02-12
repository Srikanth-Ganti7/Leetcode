class Solution:
    def isValid(self, s: str) -> bool:
        left = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                left.append(c)
            else:
                if len(left) == 0:
                    return False
            
                else:
                    value = left.pop()

                    if value == "(" and c != ")":
                        return False
                    
                    elif value == "{" and c != "}":
                        return False
                    
                    elif value == "[" and c!= "]":
                        return False
        return len(left) == 0

        
        