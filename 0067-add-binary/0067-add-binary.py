class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        decimalA = int(a, 2)
        decimalB = int(b,2)

        decimalSum = decimalA + decimalB

        binaryResult = bin(decimalSum)[2:]

        return binaryResult