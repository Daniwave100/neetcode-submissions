class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = []
        for val in nums:
            if val in vals:
                return True
            vals.append(val)

        return False