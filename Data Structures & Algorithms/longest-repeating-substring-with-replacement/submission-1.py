class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        ret = 0

        l = 0

        for r in range(len(s)):
            window_length = r - l + 1

            if s[r] not in counter:
                counter[s[r]] = 1
            else:
                counter[s[r]] += 1

            # valididy checker
            while (window_length - max(counter.values())) > k:
                print(l)
                counter[s[l]] -= 1
                l += 1
                window_length = r - l + 1
            

            ret = max(ret, window_length)
        return ret

