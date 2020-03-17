import cv2

img = cv2.imread('ee.png', 0)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

cv2.imshow('converted gray', img)

cv2.imwrite('img/test.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

