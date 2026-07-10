'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]'''



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        l=[]
        candidates.sort()

        def f(i,c,v):
            if c==target:
                l.append(v)
                return
            if c>target or i==n:
                return
            f(i+1,c+candidates[i],v+[candidates[i]])
            j=i+1
            while j<n and candidates[j]==candidates[i]:
                j+=1
            f(j,c,v)

        f(0,0,[])
        return l