import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        a = s.split()
        a = ''.join(a)
        return a.lower() == a.lower()[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


