class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for y in range(1, len(nums)):
                if i == y:
                    continue
                if (nums[i] + nums[y]) == target:
                    return [i, y]