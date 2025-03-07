import cv2
from ultralytics import YOLO

def run():
    # Load the YOLOv8 segmentation model
    model = YOLO('yolov8x-seg.pt')

    # Initialize the video capture object
    cap = cv2.VideoCapture("d:\\videaZKurniku\\19_39_43_28_09_2024.mp4")



    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform inference on the frame
        results = model(frame)

        # Annotate the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        annotated_frame = cv2.resize(annotated_frame, (1280, 768))
        cv2.imshow('Segmentation', annotated_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


run()