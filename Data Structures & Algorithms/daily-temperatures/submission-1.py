class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []
        index1 = 0
        
        while index1 < len(temperatures):
            found_anything = False
            counter = 0
            index2 = 0

            if index1 == len(temperatures) - 1:
                print("test")
                result.append(0)
                return result


            while index2 <= index1:
                index2 += 1

            while index2 < len(temperatures):
                if temperatures[index2] <= temperatures[index1]:
                    counter += 1
                else:
                    counter += 1
                    found_anything = True
                    result.append(counter)
                    break
                index2 += 1
            
            if found_anything == False:
                result.append(0)
            else:
                found_anything = False
            index1 += 1
        
        return result

