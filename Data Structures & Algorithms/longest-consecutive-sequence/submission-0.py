class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Design Idea:
        # Create a hash set 
        # Create count
        # Create a While loop
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest