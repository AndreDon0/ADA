def cyclic_shift_left(array, shift):
    shift = shift % len(arr)
    return array[shift:] + array[:shift]


n = int(input())
arr = input().split()
shifted_arr = cyclic_shift_left(arr, 2)
print(*shifted_arr)
