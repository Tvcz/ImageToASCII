from time import sleep

ascii_video_path = "sample.txt"

input_frame_rate = 30
target_frame_rate = 30

frame_rate = input_frame_rate / (int(input_frame_rate/target_frame_rate))

with open(ascii_video_path, "r") as file:
    video = file.read().split("\n\n-=-\n\n")

print(f"\nPlaying {ascii_video_path} at {frame_rate} frame(s) per second...\n")

for frame in video:
    print("\n" + frame + "\n")
    sleep(1.0/frame_rate)