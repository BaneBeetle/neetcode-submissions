class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        from collections import defaultdict

        hash_map = defaultdict(int)

        longest = 0

        left = 0
        right = 0

        while right < len(s):

            if hash_map[s[right]] == 0:
                hash_map[s[right]] = 1
            else:
                # Duplicate found
                # While invalid...
                while left <= right:
                    hash_map[s[left]] -= 1

                    if s[left] == s[right]:
                        left += 1
                        break
                    left += 1
                hash_map[s[right]] = 1

            longest = max(longest, right - left + 1)

            right += 1
            
        return longest
