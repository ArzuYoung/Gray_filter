from PIL import Image
import numpy as np


def get_gradation_step(gr_scale):
    return 255 / (gr_scale - 1)


def get_average_bright(img, y, x, step):
    sum_bright = np.sum((img[y: y + step, x: x + step]) / 3)
    return int(sum_bright // (step * step))


def change_picture(y_stop, x_stop, step, img_arr, grad_step):
    for y in range(0, y_stop, step):
        for x in range(0, x_stop, step):
            aver_bright = get_average_bright(img_arr, y, x, step)
            img_arr[y: y + step, x: x + step] = int(aver_bright // grad_step) * grad_step
    return img_arr


def make_gray_picture(img_arr, mosaic_size, grayscale):
    height = len(img_arr)
    width = len(img_arr[0])
    gradation_step = get_gradation_step(grayscale)
    return change_picture(
        height - mosaic_size + 1,
        width - mosaic_size + 1,
        mosaic_size,
        img_arr,
        gradation_step)


img = Image.open("test.jpg")
m_size = 10
g_count = 50
res_name = "res_with_filename.jpg"
img_array = np.array(img)
make_gray_picture(img_array, m_size, g_count)
res = Image.fromarray(img_array)
res.save(res_name)
