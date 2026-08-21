import cv2

# Read image
image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

# Get image properties
height, width, channels = image.shape
size = image.size
data_type = image.dtype

print("Image Properties")
print("----------------")
print("Width       :", width)
print("Height      :", height)
print("Channels    :", channels)
print("Total Pixels:", width * height)
print("Total Values:", size)
print("Data Type   :", data_type)

# Display image
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()