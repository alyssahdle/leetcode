class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # find greatest first

        greatest = 0
        for i in candies:
            if i > greatest:
                greatest = i

        result = []

        for i in candies:
            result.append(i + extraCandies >= greatest)
            
        return result

        
        