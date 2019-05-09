import numpy as np
from itertools import product


def get_fuel_amount(serial_num, n):

    def get_digit(number, n):
        return number // 10**(n - 1) % 10

    y_coord_mtx = np.reshape(np.repeat(np.arange(1, 301), 300), [300, 300])
    x_coord_mtx = y_coord_mtx.T

    step1 = x_coord_mtx + 10
    step2 = step1 * y_coord_mtx
    step3 = step2 + serial_num
    step4 = step1 * step3
    step5 = np.asarray([get_digit(step4[y_idx, x_idx], 3) for y_idx, x_idx in product(range(step4.shape[0]), range(step4.shape[1]))]).reshape(300, 300)
    step6 = step5 - 5

    return step6


def valid_conv(image, window):
    img_dim = np.shape(image)
    window_dim = np.shape(window)

    output = np.empty((img_dim[0] - window_dim[0] + 1,
                       img_dim[1] - window_dim[1] + 1))

    for y, x in product(range(img_dim[0] - 2), range(img_dim[1] - 2)):
        output[y, x] = np.sum(np.multiply(image[y:y + window_dim[0], x:x + window_dim[1]], window))
    return output


input = 4172
out = get_fuel_amount(input, 3)
window = np.ones([3, 3])
out = valid_conv(out, window)
print(np.unravel_index(np.argmax(out), out.shape))
