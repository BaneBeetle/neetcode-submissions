class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # initializations 
        left = 0

        d = {}
        d2 = {}
        # creating a copy so we can look back
        for c in s1:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        # {a: 1, b: 1, c: 1}


        # go through the string
        for right in range(len(s2)):
            if s2[right] not in d:
                left = right
                left += 1
                # reset the dictionary
                d = {}
                for c in s1:
                    if c not in d:
                        d[c] = 1
                    else:
                        d[c] += 1
            else:
                # if it is in the dictionary
                # check if the value is 0
                if d[s2[right]] == 0:
                    # make left find whatever just now made it invalid
                    while s2[left] != s2[right]:
                        d[s2[left]] += 1
                        left += 1

                    left += 1
                    d[s2[right]] += 1
                    

                d[s2[right]] -= 1
                if sum(d.values()) == 0:
                    return True

        if sum(d.values()) == 0:
            return True
        #print(list(d.values()) == [0] * len(s1))
        return False
        