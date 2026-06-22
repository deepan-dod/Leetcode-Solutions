'''Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1'''




class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]