'''A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]'''



class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            if i<=9:
                l.append(i)
            else:
                s=i
                while s>0:
                    d=s%10
                    if d==0 or i%d!=0:
                        break
                    s=s//10
                if s==0:
                    l.append(i)
        return l