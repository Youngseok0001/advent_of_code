# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Ignore This
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
# ---

# +
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

    for y, x in product(range(img_dim[0] - window_dim[0] + 1), range(img_dim[1] - window_dim[1] + 1)):
        output[y, x] = np.sum(np.multiply(image[y:y + window_dim[0], x:x + window_dim[1]], window))
    return output


def which_filter(image):

    answers = []
    for i in reversed(range(301, 1)):
        if i % 10 == 0:
            print("filter_size of {} is being computed".format(i))
        window = np.ones([i, i])
        out = valid_conv(image, window)
        argmax_idx = np.unravel_index(np.argmax(out),out.shape)
        answer = [out[argmax_idx[0],argmax_idx[1]],argmax_idx]
        answer.append(i)
        answers.append(answer)
        print(answer)
    print("done!")
    return answers


input = 4172
out = get_fuel_amount(input, 3)
answers = which_filter(out)
max_idx = max([answer[0] for answer in answers])
print([answer for answer in answers if answer[0] == max_idx])
# -


