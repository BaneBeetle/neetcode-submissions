class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Can use a hashmap to keep track of window's frequencies
        from collections import defaultdict

        hash_map = defaultdict(int)

        # two pointers
        # right keeps expanding until invalid
        # left keeps shrinking until valid
        # Would also be helpful to keep track of mismatches
        mismatch = 0
        longest = 0 # Keep track of our longest substring

        right = 0
        left = 0

        while right < len(s):

            hash_map[s[right]] += 1
            most_frequent = sorted(hash_map.items(), key=lambda item: item[1], reverse = True)[0]
            mismatch = sum(hash_map.values()) - hash_map[most_frequent[0]]
            if mismatch > k:
                hash_map[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1) 
            right += 1
        
        return longest