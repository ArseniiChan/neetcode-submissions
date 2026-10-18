class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in hmap:
                return [hmap[compliment], i]
            hmap[n] = i
        return