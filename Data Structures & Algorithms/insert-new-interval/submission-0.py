class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        is_not_appended = True

        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if is_not_appended:
                    res.append(newInterval)
                    is_not_appended = False
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if is_not_appended:
            res.append(newInterval)
            
        return res