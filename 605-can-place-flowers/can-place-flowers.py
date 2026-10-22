class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        # for each plot, check if a flower can be planted
        for i in range(len(flowerbed)):
            # boolean variables to indicate if empty
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True
        
        return False


            
        # if the number of flowers that can be planted >= n, true