class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i=0
        while i<n:
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    return [i, j]
            i+=1
                