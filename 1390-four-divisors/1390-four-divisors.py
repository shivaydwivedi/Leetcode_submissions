class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        total = 0

        for x in nums:
            # Case 1: p^3
            p = round(x ** (1/3))
            if p ** 3 == x and is_prime(p):
                total += 1 + p + p*p + x
                continue

            # Case 2: p * q
            for d in range(2, int(x ** 0.5) + 1):
                if x % d == 0:
                    a, b = d, x // d
                    if a != b and is_prime(a) and is_prime(b):
                        total += 1 + a + b + x
                    break

        return total
