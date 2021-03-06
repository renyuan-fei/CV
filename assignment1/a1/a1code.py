### Supporting code for Computer Vision Assignment 1
### See "Assignment 1.ipynb" for instructions

import math

import numpy as np
from skimage import io


def load (img_path):
    """Loads an image from a file path.

    HINT: Look up `skimage.io.imread()` function.
    HINT: Converting all pixel values to a range between 0.0 and 1.0
    (i.e. divide by 255) will make your life easier later on!

    Inputs:
        image_path: file path to the image.

    Returns:
        out: numpy array of shape(image_height, image_width, n_channels).
    """
    out = None

    # read image by path
    img_io = io.imread (img_path)

    # convert image to matrix
    # 创建数组，并将值控制在0~255之间
    np_img = np.array (img_io) / 255
    # np_img = np.asarray (np_img, dtype=np.float32)
    #
    # width = np_img.shape[0]
    # height = np_img.shape[1]
    #
    # for i in range (width):
    #     for j in range (height):
    #         np_img[i][j] = np_img[i][j] / 255

    out = np_img
    return out


def print_stats (image):
    """ Prints the height, width and number of channels in an image.
        
    Inputs:
        image: numpy array of shape(image_height, image_width, n_channels).
        
    Returns: none
                
    """
    SHAPE = image.shape

    # YOUR CODE HERE
    if len (SHAPE) == 3:
        # height
        print ('Height:', SHAPE[0])
        # width
        print ('Width:', SHAPE[1])
        # channels
        print ('Channels:', SHAPE[2], "\n")
    else:
        # height
        print ('Height:', SHAPE[0])
        # width
        print ('Width:', SHAPE[1])
        # channels
        print ('Channels:', 1, "\n")

        # print (SHAPE)

    return None


def crop (image, x1, y1, x2, y2):
    """Crop an image based on the specified bounds. Use array slicing.

    Inputs:
        image: numpy array of shape(image_height, image_width, 3).
        (x1, y1): the coordinator for the top-left point
        (x2, y2): the coordinator for the bottom-right point
        

    Returns:
        out: numpy array of shape(x2 - x1, y2 - y1, 3).
    """

    out = None

    # crop the origin array
    #                  x1~x2    y1~y2   step=1
    # crop_image = image[x1:x2, y1:y2]

    temp = image

    crop_image = temp[y1:y2, x1:x2]

    out = np.array (crop_image)

    return out


def resize (input_image, fx, fy):
    """Resize an image using the nearest neighbor method.
    Not allowed to call the matural function.
    i.e. for each output pixel, use the value of the nearest input pixel after scaling

    Inputs:
        input_image: RGB image stored as an array, with shape
            `(image_height, image_width, 3)`.
        fx (float): the resize scale on the original width.
        fy (float): the resize scale on the original height.

    Returns:
        np.ndarray: Resized image, with shape `(image_height * fy, image_width * fx, 3)`.
    """
    out = None

    image = input_image.shape

    # get width and height
    # 获取宽 高
    if len(input_image.shape) == 3:
        height = image[0]
        width = image[1]
        channel = image[2]
    else:
        height = image[0]
        width = image[1]
        channel = 1

    # 将宽高转化成int类型，用于遍历
    new_width = int (fx * width)
    new_height = int (fy * height)

    # create a new image
    # 根据新的 高 ， 宽 创建全0矩阵
    new_image = np.zeros ((new_height, new_width, channel))

    # traverse
    # 开始遍历
    for i in range (new_height):
        for j in range (new_width):
            # get the nearest pixel in orginal image
            # 获取在原始图片中最近的值
            src_x = round ((i * (1 / fy)))
            src_y = round ((j * (1 / fx)))

            # 将获取到的值放入新的图片
            # 当值大于边界时，将其设为边界（防止超出边界）
            if src_x >= height: src_x = height - 1
            if src_y >= width: src_y = width - 1

            new_image[i, j] = input_image[src_x, src_y]

    out = new_image

    return out


def change_contrast (image, factor):
    """Change the value of every pixel by following

                        x_n = factor * (x_p - 0.5) + 0.5

    where x_n is the new value and x_p is the original value.
    Assumes pixel values between 0.0 and 1.0 
    If you are using values 0-255, divided by 255.

    Inputs:
        image: numpy array of shape(image_height, image_width, 3).
        factor (float): contrast adjustment

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None

    new_image = factor * (image - 0.5) + 0.5
    out = np.array (new_image)

    return out


def greyscale (input_image):
    """Convert a RGB image to greyscale. 
    A simple method is to take the average of R, G, B at each pixel.
    Or you can look up more sophisticated methods online.
    
    Inputs:
        input_image: RGB image stored as an array, with shape
            `(image_height, image_width, 3)`.

    Returns:
        np.ndarray: Greyscale image, with shape `(image_height, image_width)`.
    """

    # GRAY = 0.3 * R + 0.59 * G + 0.11 * B

    out = None

    # 转换成2D矩阵
    # grey_img = 0.2126 * input_image[:, :, 0] + 0.7152 * input_image[:, :, 1] + 0.0722 * input_image[:, :, 2]

    grey_img = 0.299 * input_image[:, :, 0] + 0.587 * input_image[:, :, 1] + 0.114 * input_image[:, :, 2]

    # average
    # grey_img = (input_image[:, :, 0] + input_image[:, :, 1] + input_image[:, :, 2]) / 3

    out = np.array (grey_img)

    return out


def binary (grey_img, th):
    """Convert a greyscale image to a binary mask with threshold.
  
                  x_n = 0, if x_p < th
                  x_n = 1, if x_p > th
    
    Inputs:
        input_image: Greyscale image stored as an array, with shape
            `(image_height, image_width)`.
        th (float): The threshold used for binarization, and the value range is 0 to 1
    Returns:
        np.ndarray: Binary mask, with shape `(image_height, image_width)`.
    """
    out = None

    height, width = grey_img.shape

    new_img = np.zeros (grey_img.shape)

    for i in range (0, height - 1):
        for j in range (0, width - 1):
            if grey_img[i, j] < th:
                new_img[i, j] = 0
            else:
                new_img[i, j] = 1

    return np.array (new_img)


def conv2D (image, kernel):
    """ Convolution of a 2D image with a 2D kernel. 
    Convolution is applied to each pixel in the image.
    Assume values outside image bounds are 0.
    
    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi).
    """

    out = None

    # 获取kernel的height 和 width用于inverse
    ker_height, ker_width = kernel.shape

    height, width = image.shape

    # 边框填充0
    # 上下
    for i in range (int (ker_height / 2)):
        image = np.insert (image, 0, [0], axis=0)
        image = np.insert (image, height + i + 1, [0], axis=0)

    # 左右
    for i in range (int (ker_width / 2)):
        image = np.insert (image, 0, [0], axis=1)
        image = np.insert (image, width + i + 1, [0], axis=1)

    # 458 749
    # image = np.insert (image, 0, [0], axis=0)
    # image = np.insert (image, height + 1, [0], axis=0)
    #
    # image = np.insert (image, 0, [0], axis=1)
    # image = np.insert (image, width + 1, [0], axis=1)

    # 构建空array
    new_image = []

    # 反转kernel
    # for i in range (ker_height - 1):
    #     for j in range (ker_width - i - 1):
    #         temp = kernel[i, j]
    #         kernel[i, j] = kernel[ker_height - j - 1, ker_width - i - 1]
    #         kernel[ker_height - j - 1, ker_width - i - 1] = temp

    # temp = np.flip (kernel, axis=0)
    # kernel = np.flip (temp, axis=1)
    kernel = np.flip (kernel)

    # 卷积函数的实现
    # kernel 3 * 3
    #               height - ker_height + 1
    for i in range (height):
        line = []
        #               width - ker_width + 1
        for j in range (width):
            # 每次都获取一块3*3的区块和kernel相乘
            temp = image[i:i + ker_height, j:j + ker_width]
            # 将image的区块和kernel相乘后的结果 相加 存入line
            line.append (np.sum (np.multiply (kernel, temp)))
        # 处理玩一行后，将结果放入new_image中
        new_image.append (line)

    return np.array (new_image)


def test_conv2D ():
    """ A simple test for your 2D convolution function.
        You can modify it as you like to debug your function.
    
    Returns:
        None
    """

    # Test code written by 
    # Simple convolution kernel.
    kernel = np.array (
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 0]
                ]
            )

    # Create a test image: a white square in the middle
    test_img = np.zeros ((9, 9))
    test_img[3:6, 3:6] = 1

    # Run your conv_nested function on the test image
    test_output = conv2D (test_img, kernel)

    # Build the expected output
    expected_output = np.zeros ((9, 9))
    expected_output[2:7, 2:7] = 1
    expected_output[5:, 5:] = 0
    expected_output[4, 2:5] = 2
    expected_output[2:5, 4] = 2
    expected_output[4, 4] = 3

    # Test if the output matches expected output
    assert np.max (test_output - expected_output) < 1e-10, "Your solution is not correct."


def RGB_conv (image, kernel):
    # 创建空的array
    new_img = []

    # 获取kernel的 height 和 width
    ker_height, ker_width = kernel.shape

    # 反转kernel
    # for i in range (ker_height - 1):
    #     for j in range (ker_width - i - 1):
    #         temp = kernel[i, j]
    #         kernel[i, j] = kernel[ker_height - j - 1, ker_width - i - 1]
    #         kernel[ker_height - j - 1, ker_width - i - 1] = temp

    # temp = np.flip (kernel, axis=0)
    # kernel = np.flip (temp, axis=1)
    kernel = np.flip (kernel)

    # 获取img的 height ， width ，channel

    height, width, channel = image.shape

    # 边框填充0
    # 上下
    for i in range (int (ker_height / 2)):
        image = np.insert (image, 0, [0], axis=0)
        image = np.insert (image, height + i + 1, [0], axis=0)

    # 左右
    for i in range (int (ker_width / 2)):
        image = np.insert (image, 0, [0], axis=1)
        image = np.insert (image, width + i + 1, [0], axis=1)

    # 循环，分别对R G B每一层进行卷积操作
    #               height - ker_height + 1
    for i in range (height):
        line = []
        #               width - ker_width + 1
        for j in range (width):
            my_channel = []
            for k in range (channel):
                # 获取一层的值
                temp = image[i:i + ker_height, j:j + ker_width, k]
                # 进行卷积,并求和
                my_sum = np.sum (np.multiply (kernel, temp))
                # 将每层卷积的结果放入my_channel
                my_channel.append (my_sum)
            # 放入line
            line.append (my_channel)
        # 将line放入new_img
        new_img.append (line)

    # 返回new_img
    return np.array (new_img)


def conv (image, kernel):
    """Convolution of a RGB or grayscale image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    out = None
    # 判断是 2D 还是 3D
    SHAPE = image.shape

    if len (SHAPE) == 3:
        # RGB
        return RGB_conv (image, kernel)
    else:
        # grey
        return conv2D (image, kernel)


def gauss2D (size, sigma):
    """Function to mimic the 'fspecial' gaussian MATLAB function.
       You should not need to edit it.
       
    Args:
        size: filter height and width
        sigma: std deviation of Gaussian
        
    Returns:
        numpy array of shape (size, size) representing Gaussian filter
    """

    x, y = np.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    g = np.exp (-((x ** 2 + y ** 2) / (2.0 * sigma ** 2)))
    return g / g.sum ()


def corr (image, kernel):
    """Cross correlation of a RGB image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    out = None

    # new_kernel = np.flip (kernel, axis=0)
    # new_kernel = np.flip (new_kernel, axis=1)
    new_kernel = np.flip (kernel)

    out = conv (image, new_kernel)

    return out
