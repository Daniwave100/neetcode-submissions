class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                return True
                # my_dict[nums[i]] = my_dict[nums[i]] + 1
            # if not in dict, add as new key with += 1. if in dict, add to val
        

        return False