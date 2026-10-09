class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for letter in s:
            if letter.isalnum():
                new_s += letter
        
        new_s = new_s.casefold()

        return new_s == new_s[::-1]
        