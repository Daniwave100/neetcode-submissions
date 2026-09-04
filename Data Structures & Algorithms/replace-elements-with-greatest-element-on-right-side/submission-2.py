class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        max_val = arr[-1]
        x = 0

        while i > -1:
            x = arr[i]
            arr[i] = max_val
            if x > max_val:
                max_val = x
                

            i -= 1
            print(arr)

        arr[-1] = -1
        return arr