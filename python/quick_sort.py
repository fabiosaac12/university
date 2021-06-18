array = [4, 7, 2, 8, 3, 1, 8, 9, -2, 12, -3, -5]

def sort(arr):
    if len(arr) > 1:
        pivot = arr[0]

        left_arr = []
        right_arr = []

        for num in arr:
            if num < pivot:
                left_arr.append(num)
            elif num > pivot:
                right_arr.append(num)

        left_arr_sorted = sort(left_arr)
        right_arr_sorted = sort(right_arr)

        return [*left_arr_sorted, pivot, *right_arr_sorted]

    return arr

sorted_array = sort(array)

print(sorted_array)
