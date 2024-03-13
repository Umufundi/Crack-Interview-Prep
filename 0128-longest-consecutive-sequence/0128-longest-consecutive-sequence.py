class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setSeen = set(nums)
        maxCount = 0
        maxElem = len(nums)
        for n in setSeen:
            if n in setSeen:
                if(n-1) not in setSeen:
                    count = 1
                    while n+count in setSeen:
                        count += 1
                    maxCount = count if maxCount < count else maxCount
            if maxCount == maxElem:
                return maxCount
        return maxCount