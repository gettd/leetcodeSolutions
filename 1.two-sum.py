#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int] 
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if i!=j and sum == target:
                    return [i, j]
    
# @lc code=end

