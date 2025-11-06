class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate over the array 
        for i in range(len(flowerbed)):
            # check if that index(plot) is empty 
            if flowerbed[i] == 0:
                # check if the left neighbor plots are empty
                left_empty = (i== 0) or (flowerbed[i-1]==0)
                # check if right neighbor plots are empty
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            # if plots are empty in neighbor
                if left_empty and right_empty:
                    # mark the flowerbed is 1
                    flowerbed[i] = 1
                    # Decrement n by 1
                    n = n-1
            # if n is less than zero at any point 
            if n <= 0:
                # just say True
                return True
        return n<= 0


         