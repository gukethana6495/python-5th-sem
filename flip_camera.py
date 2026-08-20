import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

flip_mode = 0

print("Camera started!")
print("H = Horizontal flip")
print("V = Vertical flip")
print("B = Both flips")
print("N = Normal")
print("Q = Quit")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot read camera")
        break

    # Apply selected flip
    if flip_mode == 1:
        display = cv2.flip(frame, 1)

    elif flip_mode == 2:
        display = cv2.flip(frame, 0)

    elif flip_mode == 3:
        display = cv2.flip(frame, -1)

    else:
        display = frame

    cv2.imshow("Flip Camera", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('h'):
        flip_mode = 1

    elif key == ord('v'):
        flip_mode = 2

    elif key == ord('b'):
        flip_mode = 3

    elif key == ord('n'):
        flip_mode = 0

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()