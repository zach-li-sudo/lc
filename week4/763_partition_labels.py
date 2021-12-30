def partitionLabels(s):
    # step 1: find position intervals for each letter
    hashmap = dict()
    for i in range(len(s)):
        ch = s[i]
        if ch not in hashmap:
            hashmap.update({ch: [i]})
        else:
            hashmap[ch].append(i)
    for key in hashmap.keys():
        hashmap[key] = [hashmap[key][0], hashmap[key][-1]]

    intervals = list(hashmap.values())
    # print(intervals)

    # step 2: merge intervals
    results = [intervals[0]]
    for interval in intervals[1:]:
        current = results[-1]
        if interval[0] > current[1]: # no overlap
            results.append(interval)
        else:
            results[-1] = [min(current[0], interval[0]), max(current[1], interval[1])]
        # print(results)

    return [r[-1] - r[0] + 1 for r in results]


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))