class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = 0
        i = 1
        while x < n:
            x += i
            i += 1
        if x == n:
            return i - 1
        else:
            return i - 2