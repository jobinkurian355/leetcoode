class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if num == rev:
            return True
        else:
            return False        