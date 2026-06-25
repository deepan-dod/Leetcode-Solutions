'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.'''



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero=0
        l=0
        m=0
        for r in range(len(nums)): 
            if nums[r]==0:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero<=k:
                m=max(m,r-l+1)
        return m