class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = intervals + [newInterval]

        intervals = sorted(new, key = lambda x:x[0])

        ans=[[-1,-1]]

        for i in range(len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                (x, y) = ans.pop()
                ans.append([x, max(y, intervals[i][1])])
            else:
                ans.append(intervals[i])
            
        return ans[1:]