class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        possible_arrays = []

        for row in matrix:
            if row[0] <= target:
                possible_arrays.append(row)
        
        for rows in possible_arrays:
            for e in rows:
                if e == target:
                    return True
        return False