def qs(arr: list[int], lo: int, hi: int) -> None:
    """
    Helper function for quick sort
    :param arr:  array to be sorted
    :param lo:  lower bound of the array
    :param hi:  upper bound of the array
    :return:  None
    """
    if lo >= hi:
        return

    pivotIdx = partition(arr, lo, hi)

    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    """
    Partitions the array into two parts, one with values less than the pivot and one with values greater than the pivot
    :param arr:  array to be partitioned
    :param lo:  lower bound of the array
    :param hi:  upper bound of the array
    :return:  the index of the pivot
    """
    pivot: int = arr[hi]

    idx: int = lo - 1

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp

    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int]) -> None:
    """
    Sorts an array using quick sort
    :param arr:  array to be sorted
    :return:  None
    """
    qs(arr, 0, len(arr) - 1)


test_list: list[int] = [3, 7, 8, 5, 10, 6, 11, 3, 7, 23, 12]

quick_sort(test_list)

print(test_list)

# How does quicksort algorithm work:
# It breaks a large array into smaller ones
# A pivot is selected and the pivot is used to break the array into two parts
