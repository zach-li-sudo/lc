def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = j = k = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            nums1[k] = nums1[i]
            k += 1
            i += 1
            j += 1
    
    return nums1[:k]


# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))