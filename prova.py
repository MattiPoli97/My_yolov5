import cv2
import matplotlib.pyplot as plt

image = cv2.imread("ckcu8ty6z00003b5yzfaezbs5.jpg")
print(image.shape)
img_w = image.shape[1] #x
img_h = image.shape[0] #y
x = 0.702474
y = 0.682292
w = 0.272135
h = 0.586806
x = int(x * img_w)
y = int(y * img_h)
w = int(w * img_w)
h = int(h * img_h)

image1 = cv2.rectangle(image, (int(x-w/2),int(y-h/2)), (int(x+w/2),int(y+h/2)), (255, 0, 0), 3)
#image1 = cv2.rectangle(image, (180,20), (316,191), (255, 0, 0), 3)
plt.imshow(image1)
plt.show()


