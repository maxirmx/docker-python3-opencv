import numpy as np
import cv2


print("Running cv2 " + cv2.__version__)

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow('image', img)
print("Now press any key at X Terminal")
cv2.waitKey(0)
print("Bye-bye, my friend ...")
