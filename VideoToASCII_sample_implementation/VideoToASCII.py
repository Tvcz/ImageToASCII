from ImageToASCII import ImageToASCII
import cv2
from pathlib import Path
import time

try:
    video_path = "sample.gif"

    video = cv2.VideoCapture(video_path)
    ascii = ImageToASCII()

    ascified_video = []

    frame_count = 0
    input_frame_rate = 30
    target_frame_rate = 30

    while(video.isOpened()):

        ret, frame = video.read()
        if ret == False:
            print("Failed to retrieve frame. Exiting...")
            break


        if frame_count % (int(input_frame_rate / target_frame_rate)) == 0:
            ascified_frame = ascii.ascify(width=1000, image=frame, black_limit=20)
            ascified_video.append(ascified_frame)

            print(f"\nFrame {frame_count} ascified. Continuing...")

        frame_count += 1

finally:
    video.release()
    cv2.destroyAllWindows()

    output_file = f"{Path(video_path).stem}.txt"

    with open(output_file, "w+") as file:
        for image in ascified_video:
            for row in image:
                file.write("".join(row) + "\n")
            file.write("\n-=-\n\n")        

    print(f"\nOutput saved to \"{output_file}\"")

