import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hemker.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Kerner untuk sharphening
kernel = np.array([[-1,-1,-1],
                  [-1,9,-1],
                  [-1,-1,-1]])

dst = cv2.filter2D(img,-1,kernel)

#Smoothing menggunakan median
median = cv2.medianBlur(img, 5)

#Smoothing menggunakan filter gaussian
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dst), plt.title('Sharpening')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(median), plt.title('Median Filtering')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(gaussian), plt.title('Gaussian Filtering')
plt.xticks([]), plt.yticks([])
plt.show()
