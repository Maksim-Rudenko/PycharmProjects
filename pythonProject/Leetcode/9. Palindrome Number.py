class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        y_str = ''
        for i in range(len(x_str)):
            y_str += x_str[len(x_str) - i - 1]
        return x_str == y_str


