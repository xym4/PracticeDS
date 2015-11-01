def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = int(len(lst) / 2)
        left = mergesort(lst[:mid])
        right = mergesort(lst[mid:])
        return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

print(mergesort([10, 3, 4, 5, 8, 3, 29, 32, 7]))