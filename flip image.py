import cv2 as cv

img = cv.imread('house.jpg')

if img is None:
    print('Error: Image could not be loaded.')
else:
    horizontal_flip = cv.flip(img, 1)
    vertical_flip = cv.flip(img, 0)
    both_flip = cv.flip(img, -1)
    rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

    cv.imshow('Original Image', img)
    cv.imshow('Horizontal Flip', horizontal_flip)
    cv.imshow('Vertical Flip', vertical_flip)
    cv.imshow('Both Flip', both_flip)
    cv.imshow('Rotated Image', rotated)

    cv.waitKey(0)
    cv.destroyAllWindows()