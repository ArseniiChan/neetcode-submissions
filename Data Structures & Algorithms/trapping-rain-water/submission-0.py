class Solution:
    def trap(self, height: List[int]) -> int:
        #pre: height an array of non negative integers
        #post: trap returns the max area of water trapped

        #thought process 
        #have 2 pointers 
        #l = 0, r = l + 1
        leftMax = [0] * len(height)
        leftMax[0] = height[0]

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]

        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        total = 0

        for i in range(len(height)):
            water_at_i = min(leftMax[i], rightMax[i]) - height[i]
            total += water_at_i

        return total
        