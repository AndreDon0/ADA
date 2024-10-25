import numpy as np
import sys


def get_nearest(array: np.ndarray) -> int:
    sign_array = np.sign(array)
    abs_array = np.abs(array)
    index_arr_min = np.argmin(abs_array)
    return int(sign_array[index_arr_min] * abs_array[index_arr_min])


arr = np.loadtxt(sys.stdin)
print(get_nearest(arr))
