class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initializations
        # here I would two pointers

        l = 0
        substring = set()
        longest = 0

        for r in range(len(s)):

            # if we find a duplicate...
            while s[r] in substring and len(substring) > 0:
                substring.remove(s[l])
                l += 1

            # if we dont find a duplicate...
            substring.add(s[r])
            longest = max(longest, len(substring))
        return longest
     
        