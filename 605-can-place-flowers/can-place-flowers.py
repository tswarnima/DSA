class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        l = len(flowerbed)
        ans = 0

        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i-1] == 0:
                    if i == l-1 or flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        ans += 1

            if ans >= n:
                return True

        return False