class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Step 1: Calculate something about the entire array first
        total_sum = sum(nums)

        # Step 2: As we check each index
        left_sum = 0
        for i in range(len(nums)):
            # At index i:
            # - We know left_sum (sum of everything before i)
            # - We know total_sum
            # - Can we calculate right_sum? How?
    
            right_sum = total_sum - left_sum - nums[i]
    
        # - What condition needs to be true for i to be the pivot?
            if left_sum == right_sum:
                return i
    
        # - Before moving to next index, what should we update?
            left_sum += nums[i]
            
        return -1  # No pivot found