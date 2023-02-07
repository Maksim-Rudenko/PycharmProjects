class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[len(digits) - 1] += 1
        for i in range(len(digits)):
            if digits[len(digits) - 1 - i] == 10:
                digits[len(digits) - 1 - i] = 0
                if len(digits) - 2 - i >= 0:
                    digits[len(digits) - 2 - i] += 1
        kk = 0
        for i in digits:
            kk += i
        if kk == 0:
            return [1] + digits
        else:
            return digits

prog = Solution()
prog.plusOne(digits=[1, 2])







