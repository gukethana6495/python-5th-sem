import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Draw a line
    cv.line(
        frame,
        (0, h // 2),
        (w, h // 2),
        (255, 0, 0),
        2
    )

    # Draw a rectangle
    cv.rectangle(
        frame,
        (50, 50),
        (250, 180),
        (0, 255, 0),
        2
    )

    # Draw a circle
    cv.circle(
        frame,
        (w // 2, h // 2),
        60,
        (0, 0, 255),
        3
    )

    cv.imshow("Drawing on Video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()