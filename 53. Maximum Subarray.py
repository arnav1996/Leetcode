/*

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            tmp_sum = nums[0]
            max_sum = nums[0]
            for _value in nums[1:]:
                tmp_sum = tmp_sum + _value if tmp_sum + _value > _value else _value
                max_sum = tmp_sum if tmp_sum > max_sum else max_sum
            return max_sum
        else:
            return 0
