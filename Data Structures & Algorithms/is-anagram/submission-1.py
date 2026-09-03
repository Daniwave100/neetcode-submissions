class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            # basically, we are setting the value using s_dict.get as either the current value + 1 (to count) or initialize it as 0 if key does not have value
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

 
        print(s_dict)
        print(t_dict)
        if s_dict == t_dict:
            return True
        else:
            return False

        
            