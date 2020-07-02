from math import ceil


def bin_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = lo + ceil((hi-lo) / 2)
        if arr[mid] < key:
            lo = mid + 1
        elif arr[mid] > key:
            hi = mid - 1
        else:
            return mid


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(len(arr))[1:]):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


def insertion(arr):
    for i in range(len(arr))[1:]:
        if arr[i] < arr[i-1]:
            arr[i] += arr[i-1]
            arr[i-1] = arr[i] - arr[i-1]
            arr[i] = arr[i] - arr[i-1]
    return arr


def merge(l, r):
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            j += 1
            res.append(r[j])
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(left, right)


def rank_sort(arr):
    rank_size = len(str(max(arr)))
    res = {}
    for rank in range(rank_size)[1:]:
        i = lambda x, y: x // 10**y % 10
        for v in arr:
            if i(v, rank) not in res:
                res[i(v, rank)] = [v, ]
            else:
                res[i(v, rank)].append(v)
        arr = []
        for v in res.values():
            arr += v
    return arr


a = [22, 3, 7, 1, 78]

print(bubble_sort(a))
print(insertion(a))
print(merge_sort(a))
a = rank_sort(a)
print(a)
print(bin_search(a, 3))
