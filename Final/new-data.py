import glob
import PIL.Image as Image
import os
from torchvision import transforms as transforms

if __name__ == '__main__':
    paths = glob.glob('./new-dataset/TRAIN/scissors/*.png')
    outfile = './new-dataset/TRAIN/scissors/'

    num = 0

    for path in paths:
        im = Image.open(path)

        new_im = transforms.RandomHorizontalFlip(p=1)(im)   # p表示概率
        new_im.save(os.path.join(outfile, f'Augmented data{num}.png'))
        num += 1
        print(num)

        new_im = transforms.RandomVerticalFlip(p=1)(im)
        new_im.save(os.path.join(outfile, f'Augmented data{num}.png'))
        num += 1
        print(num)

        new_im = transforms.RandomRotation(45)(im)    #随机旋转45度
        new_im.save(os.path.join(outfile, f'Augmented data{num}.png'))
        num += 1
        print(num)

    print('done')
