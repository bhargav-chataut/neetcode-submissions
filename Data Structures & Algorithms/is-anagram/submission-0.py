from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_characters = defaultdict(int)
        t_characters = defaultdict(int)
        for i in s:
            s_characters[i]+=1
        for j in t:
            t_characters[j]+=1
        if t_characters == s_characters:
            return True
        return False
