class Solution:
    def addDigits(self, num: int) -> int:
        num_out = 0
        while 9 < num:
            num = str(num)
            for i in num:
                num_out += int(i)
            num = num_out
            num_out = 0
        return num

