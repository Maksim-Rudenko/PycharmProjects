class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for i in range(len(columnTitle)):
            number += (ord(columnTitle[i]) - 64) * 26 ** (len(columnTitle) - i - 1)
        return number
