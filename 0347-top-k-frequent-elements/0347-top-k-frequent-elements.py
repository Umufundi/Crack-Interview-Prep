class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1
        
        counts = {}
        for key, v in frequency.items():
            if v not in counts:
                counts[v] = [key]
            else:
                counts[v].append(key)
        
        counts_sorted = sorted(list(counts.keys()))

        result = []
        for count in reversed(counts_sorted):
            for c in counts[count]:
                result.append(c)
                if len(result) == k:
                    return result

        return result