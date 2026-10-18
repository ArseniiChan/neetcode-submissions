class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums)):
            # optimization: sorted, so a positive first can't sum to 0
            if nums[first] > 0:
                break
            # skip duplicate first values
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s < 0:
                    second += 1
                elif s > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    # skip duplicate second values
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
        return res
        