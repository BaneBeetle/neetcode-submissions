class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Here, I think we can have 1 pointer per string
        # This way we can check to ensure we are going in order

        ptr1 = 0
        ptr2 = 0

        # s is the sub, t is the long

        while ptr1 < len(t):
            if ptr2 >= len(s):
                return True

            if s[ptr2] == t[ptr1]:
                print(s[ptr2])
                ptr2 += 1
            if ptr2 >= len(s):
                return True
                

            ptr1 += 1
        

        return False
        