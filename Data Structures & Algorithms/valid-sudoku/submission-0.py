class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        tracker = {}

        row_counter = 0
        for row in board:
            row_counter += 1
            col_counter = 0

            seen = []

            for e in row:
                col_counter += 1
                if e == ".":
                    continue
                else:
                    if e in tracker:
                        # We have seen this number before
                        # lets check if either row or col are the same
                        # then check row and col differences

                        # we will be comparing [(row_counter, col_counter), (row_counter, col_counter), (row_counter, col_counter)]

                        for saved_coord in tracker[e]:

                            # lets check if either row or col are the same
                            if row_counter == saved_coord[0]:
                                print("Same row!")
                                return False
                            if col_counter == saved_coord[1]:
                                print("Same Col!")
                                return False
                            
                            # next scenario would be to check the 9x9 
                            # check if they are in the same family
                            # We have 3 categories, rows 1-3, 4-6, 7-9
                            # do these checks for both row and columns
                            # Here, we will calculate which box they belong in. Must do r - 1 and c - 1 because i am not 0-indexed based

                            current_sector = ((row_counter - 1) // 3, (col_counter - 1) // 3)
                            check_sector = ((saved_coord[0] - 1) // 3, (saved_coord[1] - 1) // 3)

                            if current_sector == check_sector:
                                return False

                        # if it clears all our checks, add it

                        tracker[e].append((row_counter, col_counter))

                    else:
                        # will only hit if we have never seen that number before
                        tracker[e] = [(row_counter, col_counter)]
        
        return True
        