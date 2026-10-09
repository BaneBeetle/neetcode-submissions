class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # My first instinct is to initiate a hash to count
        # Then add em all up later

        from collections import defaultdict

        counts = defaultdict(int) # Will count num letters
        ret = ""
        left_over = ""

        for letter in s:
            counts[letter] += 1
            if letter not in order:
                left_over += letter


        print(counts)

        for c in order:
            ret += c * counts[c]
        
        return ret + left_over

