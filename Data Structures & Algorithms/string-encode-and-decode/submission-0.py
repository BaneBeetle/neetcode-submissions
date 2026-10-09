

class Solution:

    def encode(self, strs: List[str]) -> str:
        # input: ["neet","code","love","you"]
        #  4#neet4#code#4love3#you

        ret = []
        for word in strs:
            num = len(word)

            ret.append(str(num)) # 4
            ret.append("#") # #
            ret.append(word) # neet

        ret_val = "".join(ret)
        return ret_val


        


    def decode(self, s: str) -> List[str]:
        # input: 4#neet4#code4#love3#you

        word_lst = [] # desired result: ["neet","code","love","you"]

        index = 0
        concat_str = ""
        
        while index < len(s): # Change later

            if s[index] != "#":
                concat_str += s[index]
                
            else:

                skip = int(concat_str) + (index + 1)
                word = s[index + 1 : skip]
                word_lst.append(word)

                index = skip - 1
                concat_str = ""

            index += 1
        
        return word_lst




        pass
       











