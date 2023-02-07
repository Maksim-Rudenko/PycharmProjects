class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = sum(map(lambda x: int(x) * int(x), str(n)))
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)




