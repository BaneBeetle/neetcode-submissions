class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)

        top = 0
        bottom = ROWS - 1

        while top <= bottom:

            middle_row = (top + bottom) // 2

            first = matrix[middle_row][0]
            last = matrix[middle_row][-1]

            if target > last:
                top = middle_row + 1
            elif target < first:
                bottom = middle_row - 1
            else:
                # its in this row
                print("Its in this row")
                print(target)
                search_here = matrix[middle_row]
                
                l = 0
                r = len(search_here) - 1

                while l <= r:
                    m = (l + r) // 2

                    if search_here[m] < target:
                        l = m + 1
                    elif search_here[m] > target:
                        r = m - 1
                    else:
                        return True
                
                return False

    
        return False