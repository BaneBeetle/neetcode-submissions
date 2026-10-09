class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counter = defaultdict(int)

        left = 0
        right = 0

        current_max = 0

        while right < len(s):
            # check if more than 1
            if counter[s[right]] == 1:
                # if 1, adding will make it more already
                while s[right] != s[left]:
                    counter[s[left]] -= 1
                    left += 1
    
                left += 1
                counter[s[right]] = 1
            
            else:
                counter[s[right]] = 1
    
            right += 1
            current_max = max(current_max, right - left)
    
        return current_max
