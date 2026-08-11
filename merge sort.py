def merge_arrays(arr1, arr2):
    p1, p2 = 0, 0
    merged = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1

    return merged + arr1[p1:] + arr2[p2:]



a = [1, 3, 5]
b = [2, 4, 6]
print(merge_arrays(a, b))