class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        same = set()

        for n in nums:
            if n in same:
                return True
            same.add(n)
        return False
    
            

        