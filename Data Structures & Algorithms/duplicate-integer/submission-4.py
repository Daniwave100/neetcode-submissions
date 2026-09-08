class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                return True
            my_hash[nums[i]] = i
        
        return False

            