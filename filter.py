from PIL import Image
import numpy as np


def get_gradation_step(gr_scale):
    """
    Returns gradation step in pixels
    calculated by number of gradation(grayscale)
    :param gr_scale: number of gradation
    :return: gradation step

    >>> get_gradation_step(5)
    63

    >>> get_gradation_step(10)
    28
    """
    return 255 // (gr_scale - 1)


def get_average_bright(img, y, x, step):
    """
    Returns cell average bright
    :param img: img as np.array
    :param y: start y coord
    :param x: start x coord
    :param step: size of mosaic
    :return: cell average bright
    >>> get_average_bright(np.array(Image.open("to_doctest.jpg")), 0, 0, 10)
    255
    """
    sum_bright = np.sum((img[y: y + step, x: x + step]) / 3)
    return int(sum_bright // (step * step))


def change_picture(y_stop, x_stop, step, img_arr, grad_step):
    """
    Returns changed img_arr
    :param y_stop: height - mosaic_size + 1
    :param x_stop: width - mosaic_size + 1
    :param step: mosaic_size
    :param img_arr: img as np.array
    :param grad_step: gradation step(result of get_gradation_step)
    :return: changed img_arr
    """
    for y in range(0, y_stop, step):
        for x in range(0, x_stop, step):
            aver_bright = get_average_bright(img_arr, y, x, step)
            img_arr[y: y + step, x: x + step] = int(aver_bright // grad_step) * grad_step
    return img_arr


def make_gray_picture(img_arr, mosaic_size, grayscale):
    """
    Returns modified img_arr
    :param img_arr: img as np.array
    :param mosaic_size: one cell size
    :param grayscale: number of gradation
    :return: modified img_arr
    """
    height = len(img_arr)
    width = len(img_arr[0])
    gradation_step = get_gradation_step(grayscale)
    return change_picture(
        height - mosaic_size + 1,
        width - mosaic_size + 1,
        mosaic_size,
        img_arr,
        gradation_step)


print("Enter the full name of the image:")
img = Image.open(input())
img_array = np.array(img)
print("mosaic size:")
m_size = int(input())
print("gradation count:")
g_count = int(input())
print("and the full name of the result image:")
res_name = input()
make_gray_picture(img_array, m_size, g_count)
res = (Image.fromarray(img_array)).save(res_name)

if __name__ == "__main__":
    import doctest
    doctest.testmod()