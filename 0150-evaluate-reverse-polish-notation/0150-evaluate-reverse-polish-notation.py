class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for n in tokens:
            if n not in operations:
                stack.append(n)
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if n == "+":
                    stack.append(b+a)
                
                elif n == "-":
                    stack.append(b-a)
                
                elif n == "*":
                    stack.append(b*a)
                
                elif n == "/":
                    stack.append(b/a)
        return int(stack[0])


        