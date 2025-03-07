class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1,-1]

        minE = float("infinity")

        primes = []

        def is_prime(n):
            if n <= 1:
                return False
            
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

        limit = right
        seive = [True]*(limit +1)

        seive[0] = seive[1] = False

        for i in range(2, int(limit ** 0.5) +1):
            if seive[i]:
                for j in range(i*i, limit+1, i):
                    seive[j] = False
            

        # for num in range(left, right+1):
        #     if is_prime(num):
        #         primes.append(num)

        for num in range(left,right+1):
            if seive[num]:
                primes.append(num)
        
        
        l = 0
        r = len(primes)-1

        if len(primes)<2:
            return ans

        
        for i in range(len(primes)-1):
            dist = primes[i+1] - primes[i]

            if dist < minE:
                minE = dist
                ans[0] = primes[i]
                ans[1] = primes[i+1]
        
        return ans



        