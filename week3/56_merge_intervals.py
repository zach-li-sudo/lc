def merge(intervals):
    if intervals is None:
        return None
    if len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0]) # sort by left number of each interval

    def merge_two_intervals(merged, interval):
        if len(merged) == 0:
            merged.append(interval)
            return merged
        else:
            latest = merged[-1]
            if latest[1] < interval[0]: # no-overlap
                merged.append(interval)
            else:
                latest[0] = min(latest[0], interval[0])
                latest[1] = max(latest[1], interval[1])
                merged[-1] = latest
            return merged

    merged = []
    for interval in intervals:
        merged = merge_two_intervals(merged, interval)

    return merged




# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(merge(intervals))