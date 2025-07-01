#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        lookup = set()

        for right in range(len(s)):
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1

            lookup.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length
        
# @lc code=end

