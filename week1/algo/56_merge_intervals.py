def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x:x[0])

    merged = []
    def overlap(inter1, inter2):
        if inter1[1] < inter2[0]:
            return False
        if inter2[1] < inter1[0]:
            return False
        return True
    
    def merge_intervals(inter1, inter2):
        return [min(inter2[0], inter1[0]), max(inter1[1], inter2[1])]

    for interval in intervals:
        if len(merged) == 0: # empty or on overlap
            merged.append(interval)
        elif overlap(merged[-1], interval) is False:
            merged.append(interval)
        else:
            merged[-1] = merge_intervals(merged[-1], interval)
    return merged



# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(merge(intervals))