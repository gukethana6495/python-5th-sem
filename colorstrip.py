import cv2
import numpy as np

# Create a white canvas
img = np.ones((100, 800, 3), dtype=np.uint8) * 255

# Draw color strips
cv2.rectangle(img, (0, 0), (100, 100), (0, 0, 0), -1)         # Black
cv2.rectangle(img, (100, 0), (200, 100), (255, 0, 0), -1)      # Blue
cv2.rectangle(img, (200, 0), (300, 100), (0, 255, 0), -1)      # Green
cv2.rectangle(img, (300, 0), (400, 100), (0, 0, 255), -1)      # Red
cv2.rectangle(img, (400, 0), (500, 100), (0, 255, 255), -1)    # Yellow
cv2.rectangle(img, (500, 0), (600, 100), (255, 255, 0), -1)    # Cyan
cv2.rectangle(img, (600, 0), (700, 100), (255, 0, 255), -1)    # Magenta
cv2.rectangle(img, (700, 0), (800, 100), (255, 255, 255), -1)  # White

# Display the image
cv2.imshow("Color Strip", img)

cv2.waitKey(0)
cv2.destroyAllWindows()