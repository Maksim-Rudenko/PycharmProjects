class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 0
        while x ** 2 < num:
            x += 1
        return x ** 2 == num
