class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #Case-1: Include the number
            subset.append(nums[i])
            dfs(i+1)

            #Case-2: Doesn't include the number
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
            