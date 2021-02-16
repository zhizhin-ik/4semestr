import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

k = np.array([0.299, 0.587, 0.114])
image = mpimg.imread('1212.jpg')
image_gray = np.dot(image, k)
plt.imshow(image_gray, cmap=plt.get_cmap('gray'))
plt.show()