import cv2 as cv

img = cv.imread('sample.jpg')

if img is None:
    print('Error: Image could not be loaded.')
else:
    resized = cv.resize(img, (300, 200))

    print('Original shape:', img.shape)
    print('Resized shape:', resized.shape)

    cv.imshow('Resized Image', resized)

    cv.waitKey(0)
    cv.destroyAllWindows()