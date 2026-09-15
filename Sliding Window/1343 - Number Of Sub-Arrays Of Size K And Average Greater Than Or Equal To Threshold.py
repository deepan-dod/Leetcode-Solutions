'''Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).'''



from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        m=0
        for i in range(k):
            m+=arr[i]
        if m//k>=threshold:
            c+=1
        i=1
        j=k
        while j<len(arr):
            m=m-arr[i-1]
            m=m+arr[j]
            if m//k>=threshold:
                c+=1
            i+=1
            j+=1
        return c

Solution = Solution()
arr = list(map(int, input("Enter the array of integers separated by commas: ").split(",")))
k = int(input("Enter the integer k: "))
threshold = int(input("Enter the threshold: "))
print(Solution.numOfSubarrays(arr, k, threshold))