import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        y = len(s)-1
        print(s)

        for i in range(len(s)):
            print("s", i)
            if s[i] != s[y]:
                return False

            y -= 1

        return True


