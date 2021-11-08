import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images\\cactus1.jpg", cv2.IMREAD_IGNORE_ORIENTATION)

#cv2.imshow("Cactus", img)

hist = cv2.calcHist([img], [0], None, [256], [0,256])

bin = 0
while bin < 256:
    print(hist[bin]/img.size)
    bin += 1

#plt.hist(hist)
#plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()