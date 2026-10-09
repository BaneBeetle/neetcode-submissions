class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_hash = Counter(s)
        t_hash = Counter(t)

        return s_hash == t_hash
        