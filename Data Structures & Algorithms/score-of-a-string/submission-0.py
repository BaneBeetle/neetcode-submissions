class Solution:
    def scoreOfString(self, s: str) -> int:
        # code
        # o - c, d - o, e - d
        # Each adj pair
        # I think pointers would work here

        ptr1 = 0
        ptr2 = 1 # we know min length is 2
        ret = 0

        while ptr2 < len(s):
            ret += abs(ord(s[ptr1]) - ord(s[ptr2]))

            ptr1 += 1
            ptr2 += 1

        return ret