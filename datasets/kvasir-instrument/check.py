import shutil
import os
import os.path
from os.path import isfile, join
import glob
import cv2
import matplotlib.pyplot as plt
from PIL import Image
filename = os.listdir('images_start/')
print(filename[0])
filename_1 = [i.replace('.jpg','') for i in filename]
print((len(filename_1)))

count = 0

with open("test.txt", "r") as f:
    content = f.readlines()

content = [i.replace('\n','') for i in content]
print(content)

for i in range(0, len(filename)):
    if filename_1[i] in content:
        print("test")
        count = count + 1
        shutil.move(f'images_start/{filename[i]}', 'test/images')
    else:
        print("train")
        shutil.move(f'images_start/{filename[i]}', 'train/images')

print(count)














