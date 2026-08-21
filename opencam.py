import cv2
import time

# Open webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Webcam started. Press 'q' to quit.")

# Start timer
start_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read webcam")
        break

    # Calculate elapsed time
    elapsed_time = int(time.time() - start_time)

    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60

    # Format timer as HH:MM:SS
    timer = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    # Display timer on webcam
    cv2.putText(
        frame,
        "Timer: " + timer,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("My Webcam", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()