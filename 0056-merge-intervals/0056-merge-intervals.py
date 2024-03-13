class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,len(intervals)):
            curstart=intervals[i][0]
            curend=intervals[i][1]
            if curstart<=end:
                end=max(end,curend)
            else:
                res.append([start,end])
                start=curstart
                end=curend
        
        res.append([start,end])
        return res