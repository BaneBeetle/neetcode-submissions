class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We could use counter to create anagrams 
        # But how do we store
        from collections import Counter, defaultdict


        # First lets create all possible anagrams
        seen_anagrams = []
        hash_map = defaultdict()
        for word in strs:
            x = Counter(word)
            if x not in seen_anagrams:
                seen_anagrams.append(x)
                hash_map[word] = [word]
            else:
                for key in hash_map.keys():
                    if Counter(key) == x:
                        hash_map[key].append(word)
  
        return list(hash_map.values())

