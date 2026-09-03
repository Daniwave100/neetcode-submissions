class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        answer = 0
        max_consec = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                answer += 1
                if answer > max_consec:
                    max_consec = answer
            else:
                answer = 0

                

        print(answer)
        return max_consec


