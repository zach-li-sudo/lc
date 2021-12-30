def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []
    sequence_map = dict()
    results = []
    for i in range(len(s)-9):
        ten_letter_sequence = s[i:i+10]
        if ten_letter_sequence not in sequence_map:
            sequence_map.update({ten_letter_sequence: 1})
        else:
            sequence_map[ten_letter_sequence] += 1
    
    results = []
    for key, values in sequence_map.items():
        if values >= 2:
            results.append(key)
    return results


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))