'''Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.'''




class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r=max(nums)
        m=s=1
        for i in range(len(nums)):
            t=m*nums[i]
            m=max(t,s*nums[i],nums[i])
            s=min(t,s*nums[i],nums[i])
            r=max(r,m)
        return r