import cv2

print("Testing camera...")

for camera_id in range(5):
    print("Trying camera:", camera_id)

    cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)

    if cap.isOpened():
        ret, frame = cap.read()

        if ret:
            print("Camera", camera_id, "WORKS!")

            cv2.imshow("Camera Test", frame)
            cv2.waitKey(3000)

            cap.release()
            cv2.destroyAllWindows()
            break
        else:
            print("Camera opened but cannot read frame")

    else:
        print("Camera not available")

    cap.release()

print("Test finished.")