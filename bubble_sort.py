
def bubble_sort(arr: list[int]) -> None:
    arr_length = len(arr)

    for i in range(arr_length):
        for j in range(arr_length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


test_list = [9, 3, 7, 4, 69, 420, 42]
bubble_sort(test_list)
print(test_list)
