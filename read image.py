import cv2 as cv

img = cv.imread('sample.jpg')

if img is None:
    print('Error: Image could not be loaded. Check the file path.')
else:
    print('Image loaded successfully')

    cv.imshow('Original Image', img)

    cv.imwrite('output.png', img)
    print('Image saved successfully')

    cv.waitKey(0)
    cv.destroyAllWindows()