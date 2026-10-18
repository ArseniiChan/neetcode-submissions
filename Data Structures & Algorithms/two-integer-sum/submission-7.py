class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                    # value -> the index it was at
        for i, n in enumerate(nums):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
        return []