class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        ptr1 = 0
        ptr2 = k - 1

        minimum = 99999

        while ptr2 < len(blocks):
            W_count = 0
            ptr3 = ptr1

            while ptr3 <= ptr2:
                if blocks[ptr3] == "W":
                    W_count += 1
                ptr3 += 1
            minimum = min(W_count, minimum)

            ptr2 += 1
            ptr1 += 1





        return minimum
