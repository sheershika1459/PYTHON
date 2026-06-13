class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed_x = "".join(reversed(str_x))
        return str_x == reversed_x
        