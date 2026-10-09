class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)

        sorted_counts = sorted(counts.items(), key = lambda item: item[1], reverse=True)

        ret = []

        ptr = 0
        while ptr < k:
            ret.append(sorted_counts[ptr][0])

            ptr += 1

        return ret