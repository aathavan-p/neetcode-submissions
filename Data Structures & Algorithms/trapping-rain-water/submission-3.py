class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        add = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                add += (max_l - height[l])
            
            else:
                r -= 1
                max_r = max(max_r, height[r])
                add += (max_r - height[r])
            
        return add