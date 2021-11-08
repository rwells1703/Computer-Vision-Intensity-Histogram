import cv2

img = cv2.imread("images\\cactus1.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Cactus", img)

cv2.waitKey(0)
cv2.destroyAllWindows()