class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hp = []
        count = 0
        for start, end in intervals:
            if not hp or hp[0][0] > start:
                heapq.heappush(hp, [end, start])
                count = max(count, len(hp))
            else:
                while hp and hp[0][0] <= start:
                    heapq.heappop(hp)
                heapq.heappush(hp, [end, start])
        return count