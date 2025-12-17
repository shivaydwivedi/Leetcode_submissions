class Solution:
    def closestPrimes(self, left: int, right: int):
        if right < 2:
            return [-1, -1]

        # Step 1: Sieve of Eratosthenes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        # Step 2: Collect primes in range
        primes = []
        for i in range(max(2, left), right + 1):
            if is_prime[i]:
                primes.append(i)

        # Step 3: Find closest pair
        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        ans = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap < min_gap:
                min_gap = gap
                ans = [primes[i - 1], primes[i]]

        return ans
