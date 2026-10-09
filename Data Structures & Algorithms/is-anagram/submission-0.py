class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        ptr = 0
        
        while ptr < len(s):
            
            if s_map.get(s[ptr]) is None:
                s_map[s[ptr]] = 1
            else:
                s_map[s[ptr]] += 1


            if t_map.get(t[ptr]) is None:
                t_map[t[ptr]] = 1
            else:
                t_map[t[ptr]] +=1

            ptr += 1

        
        return s_map == t_map

        