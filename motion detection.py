import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Create background subtractor
back_sub = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read camera")
        break

    # Apply background subtraction
    mask = back_sub.apply(frame)

    # Convert mask into binary image
    _, mask = cv.threshold(
        mask,
        200,
        255,
        cv.THRESH_BINARY
    )

    # Find contours
    contours, _ = cv.findContours(
        mask,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:

        # Ignore small movements/noise
        if cv.contourArea(cnt) < 1000:
            continue

        # Get bounding rectangle
        x, y, w, h = cv.boundingRect(cnt)

        # Draw rectangle around motion
        cv.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display text
        cv.putText(
            frame,
            "Motion",
            (x, y - 10),
            cv.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv.imshow("Motion Detection", frame)
    cv.imshow("Motion Mask", mask)

    # Press Q to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()