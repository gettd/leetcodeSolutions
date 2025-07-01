#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        revX = x[::-1]
        if x==revX:
            return True
        else:
            return False
        
# @lc code=end

