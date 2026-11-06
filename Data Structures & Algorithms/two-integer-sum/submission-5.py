class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in viewMap:
                return [viewMap[diff], i]
            viewMap[num] = i
        
        return []
