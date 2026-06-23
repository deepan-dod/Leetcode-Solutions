'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3'''



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        s=set(nums)
        for i in s:
            if nums.count(i)>n:
                return i