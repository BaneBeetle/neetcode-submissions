class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_anagrams = {} # key is the sorted string, value is the list

        for word in strs:
            
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word) # turns cat -> act

            if sorted_word in seen_anagrams:
                seen_anagrams[sorted_word].append(word)
            else:
                seen_anagrams[sorted_word] = [word]

        return list(seen_anagrams.values())


