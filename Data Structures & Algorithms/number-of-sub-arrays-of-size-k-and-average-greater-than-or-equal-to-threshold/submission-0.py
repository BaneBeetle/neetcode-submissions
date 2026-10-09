class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        count = 0

        current_sum = 0

        ptr2 = k - 1
        ptr1 = 0

        while ptr1 < ptr2:
            current_sum += arr[ptr1]
            ptr1 += 1

        ptr1 = 0
        while ptr2 < len(arr):

            current_sum += arr[ptr2]
            if current_sum / k >= threshold:
                count += 1
            

            ptr2 += 1
            current_sum -= arr[ptr1]
            ptr1 += 1
            
        
        return count

        