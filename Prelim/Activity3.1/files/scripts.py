import cv2

input_file = 'Rickroll.mp4'

cap = cv2.VideoCapture(input_file)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Define output formats and codecs
outputs = [
    ('rickroll_output_1.avi', cv2.VideoWriter_fourcc(*'XVID')),
    ('rickroll_output_mp4.mp4', cv2.VideoWriter_fourcc(*'mp4v')),
    ('rickroll_output_mjpg.avi', cv2.VideoWriter_fourcc(*'MJPG'))
]

# Create video writers
writers = [cv2.VideoWriter(fname, fourcc, fps, size) for fname, fourcc in outputs]

frame_count = 0
success, frame = cap.read()
while success:
    for writer in writers:
        writer.write(frame)
    frame_count += 1
    success, frame = cap.read()

cap.release()
for writer in writers:
    writer.release()

print(f"Finished writing {frame_count} frames to {len(outputs)} formats!")
