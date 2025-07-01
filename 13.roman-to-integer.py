#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        prevChar = None
        for char in s:
            if prevChar is not None and translate[char]>translate[prevChar]:
                ans -= translate[prevChar]
                ans += translate[char] - translate[prevChar]
            else:
                ans += translate[char]
            prevChar = char
        return ans
 
# @lc code=end

