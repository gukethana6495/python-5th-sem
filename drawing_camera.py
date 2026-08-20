import cv2
import numpy as np

# Open webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

canvas = None
drawing = False
last_x, last_y = -1, -1


# Mouse drawing function
def draw(event, x, y, flags, param):
    global drawing, last_x, last_y, canvas

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    # Mouse moved while button is pressed
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(
                canvas,
                (last_x, last_y),
                (x, y),
                (0, 0, 255),
                5
            )

            last_x, last_y = x, y

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_x, last_y = -1, -1


# Create window
cv2.namedWindow("Webcam Drawing")
cv2.setMouseCallback("Webcam Drawing", draw)


while True:

    # Read webcam
    ret, frame = cap.read()

    if not ret:
        print("Cannot read webcam")
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Create drawing canvas
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Put drawing on webcam
    output = cv2.add(frame, canvas)

    # Instructions
    cv2.putText(
        output,
        "Hold LEFT mouse button to draw",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        output,
        "C = Clear    Q = Quit",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Display
    cv2.imshow("Webcam Drawing", output)

    # Keyboard
    key = cv2.waitKey(1) & 0xFF

    # Clear drawing
    if key == ord("c"):
        canvas = np.zeros_like(frame)

    # Quit
    elif key == ord("q"):
        break


# Close everything
cap.release()
cv2.destroyAllWindows()