import cv2

# Open webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Webcam started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read webcam")
        break

    cv2.imshow("My Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()