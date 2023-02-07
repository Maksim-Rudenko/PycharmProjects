class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        if n >= 0:
            while 4 ** x < n:
                x += 1
            return 4 ** x == n or 4 ** (x - 1) == n
