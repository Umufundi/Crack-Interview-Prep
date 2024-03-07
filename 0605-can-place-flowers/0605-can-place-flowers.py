class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    i += 2  # Skip the next position as you cannot plant flowers consecutively
                else:
                    i += 1
            else:
                i += 2  # Skip the current position if it's already planted
        return n == 0
        