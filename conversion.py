import json
import cv2
import os
import matplotlib.pyplot as plt
import shutil

input_path = "../My_yolov5/datasets/kvasir-instrument/train/labels"
output_path = "../My_yolov5/datasets/kvasir-instrument/train"

f = open('bboxes.json')
data = json.load(f)
f.close()

x = data.keys()
print(x)
print(data['ckcx9e1ei001d3b5yr8erdyxv']['bbox'])

#images name extraction
id = []
for key in data.keys():
    id.append(key)

print(len(id)) # number of elements
print(id[0]) # name of the file
print(data[id[0]]) # all the information regarding i-file
print(data[id[0]]['height']) # height information of specific i-file
print(data[id[0]]['width']) # width information of specific i-file
print(data[id[0]]['bbox'][0]['label']) # access to label information of specific i-file
print(len(data[id[0]]['bbox'])) # number of annotation for specific i-file

count = 0

for i in range (0,len(id)): #for each data[id[i]] --> create a txt file
    # Extracting image
    img_id = id[i]
    img_w = data[id[i]]['width']
    img_h = data[id[i]]['height']

    # Opening file for current image
    file_object = open(f"{output_path}/labels/{img_id}.txt", "a")

    for ann in range(0,len(data[id[i]]['bbox'])):
        label = data[id[0]]['bbox'][0]['label']

        current_category = 0 # We have only instrument
        x = data[id[i]]['bbox'][ann]['xmin']
        y = data[id[i]]['bbox'][ann]['ymin']
        w = data[id[i]]['bbox'][ann]['xmax']
        h = data[id[i]]['bbox'][ann]['ymax']

        # Finding midpoints
        x_centre = (x + (w - x) / 2)
        y_centre = (y + (h - y) / 2)

        # Normalization
        x_centre = x_centre / img_w
        y_centre = y_centre / img_h
        w = (w-x) / img_w
        h = (h-y) / img_h

        # Limiting upto fix number of decimal places
        x_centre = format(x_centre, '.6f')
        y_centre = format(y_centre, '.6f')
        x = format(x, '.6f')
        y = format(y, '.6f')
        w = format(w, '.6f')
        h = format(h, '.6f')

        # Writing current object
        file_object.write(f"{current_category} {x_centre} {y_centre} {w} {h}\n")

    file_object.close()