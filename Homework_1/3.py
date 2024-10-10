def cyclic_shift_left(array, shift):
    shift = shift % len(arr)
    return array[shift:] + array[:shift]


n = int(input())
arr = list(map(int, input().split()))
shifted_arr = cyclic_shift_left(arr, 2)
print(" ".join(map(str, shifted_arr)))
