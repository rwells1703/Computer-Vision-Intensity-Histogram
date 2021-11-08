import cv2
import matplotlib.pyplot as plt
import numpy as np

bits_per_channel = 8
bins = 2**bits_per_channel

img = cv2.imread("images\\bubbles.jpg", cv2.IMREAD_GRAYSCALE)

#img_disp = cv2.resize(img,(1280,720))
cv2.imshow("Image", img)

hist = np.zeros(bins)

for x, y in np.ndindex((img.shape[0],img.shape[1])):
    intensity = img[x,y]
    hist[intensity] += 1/img.size

plt.plot(range(bins), hist) 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()