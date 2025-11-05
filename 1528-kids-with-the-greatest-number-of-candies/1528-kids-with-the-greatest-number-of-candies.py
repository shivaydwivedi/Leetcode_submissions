class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # max no. of candies
        max_c = max(candies)
        # empty list
        res = []
        # iterate over the loop
        for x in candies:
            if x + extraCandies >= max_c:
                res.append(True)
            else:
                res.append(False)
        return res
        