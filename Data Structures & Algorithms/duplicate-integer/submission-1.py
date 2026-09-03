class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = sorted(nums)
        print(nums2)

        x = 0
        y = len(nums2) - 1

        while x < y:
            if nums2[x] == nums2[x + 1]:
                return True
            x += 1

        return False
