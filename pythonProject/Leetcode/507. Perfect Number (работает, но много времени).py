class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        num1 = 0
        for i in range(1, num):
            if num % i == 0:
                num1 += i
        return num == num1