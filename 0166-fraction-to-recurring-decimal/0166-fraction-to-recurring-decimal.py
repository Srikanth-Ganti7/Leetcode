class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        ans = []
        if (numerator > 0 and denominator < 0) or (denominator > 0 and numerator <0):
            ans.append("-")
        
        n = abs(numerator)
        d = abs(denominator)

        ans.append(str(n//d))
        rem = n % d

        hashMap = {}

        if rem == 0:
            return "".join(ans)
        
        ans.append(".")
        
        while rem not in hashMap and rem != 0:
            hashMap[rem] = len(ans)
            rem = rem * 10

            ans += str(rem //d)
            rem = rem - d*(rem//d)
        
        if rem in hashMap:
            ans.insert(hashMap[rem], "(")
            ans.append(")")
            return "".join(ans)
        return "".join(ans)
        