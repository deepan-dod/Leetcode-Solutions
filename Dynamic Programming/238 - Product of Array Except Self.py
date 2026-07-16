'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[0]*n
        l1=[0]*n
        l[0]=1
        l1[n-1]=1
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            l1[i]=l1[i+1]*nums[i+1]
        dp=[0]*n
        for i in range(n):
            dp[i]=l[i]*l1[i]
        return dp