import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

resized = cv2.resize(image, (500, 400))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(resized, (7, 7), 0)

edges = cv2.Canny(resized, 100, 200)

cv2.imshow("Original", image)
cv2.imshow("Resized", resized)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()