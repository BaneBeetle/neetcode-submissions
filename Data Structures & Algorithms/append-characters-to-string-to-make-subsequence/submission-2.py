class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Appending to s so t can be a substring
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(s):

            if ptr2 == len(t):
                return 0

            elif s[ptr1] != t[ptr2]:
                ptr1 += 1

            else:
                # Same letter
                ptr1 += 1
                ptr2 += 1
        return len(t) - ptr2