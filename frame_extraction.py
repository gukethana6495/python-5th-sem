import cv2 as cv
import os

video_path = "input_video.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

frame_no = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    filename = os.path.join(
        output_dir,
        f"frame_{frame_no:05d}.jpg"
    )

    cv.imwrite(filename, frame)

    frame_no += 1

cap.release()

print("Total frames extracted:", frame_no)