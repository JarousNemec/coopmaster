import os
from collections import defaultdict

import cv2
from ultralytics import YOLO
import torch


class ChickenClipper:

    def __init__(self, input_video_path, output_path):
        self.video_frame_count = 0
        self.track_history = defaultdict(list)
        self.input_video_path = input_video_path
        self.save_every = 24
        self.counter = 0
        self.output_path = output_path
        self.max_frame_count = 24 * 60 * 15

    def init_task(self, input_path):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f'Using device: {device}')

        model = YOLO("yolov9e.pt").to(device)

        cap = cv2.VideoCapture(input_path)
        # # Retrieve video properties: width, height, and frames per second
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
        self.video_frame_count = 0
        return model, cap

    def save_image_frame(self, frame, stream_id):
        output_path = f'{self.output_path}/full_frame/{stream_id}/{stream_id}_{self.video_frame_count}.jpg'
        if not os.path.exists(f"{self.output_path}/full_frame/{stream_id}"):
            os.makedirs(f"{self.output_path}/full_frame/{stream_id}")
        cv2.imwrite(output_path, frame)

    def run(self):
        image_paths = [os.path.join(self.input_video_path, fname) for fname in os.listdir(self.input_video_path) if
                       fname.endswith(('.mp4', '.avi'))]
        stream_id = 0
        for image_path in image_paths:

            self.model, self.cap = self.init_task(image_path)

            while self.cap.isOpened():
                success, frame = self.cap.read()
                if not success:
                    break

                if self.video_frame_count > self.max_frame_count:
                    break

                self.counter += 1
                if self.counter % self.save_every == 0:
                    results = self.model.track(frame, persist=True, classes=14, conf=0.5)
                    self.draw_chicken(frame, results, stream_id=stream_id)
                    cv2.imshow("Chicken", frame)

                self.video_frame_count += 1
                if self.counter % self.save_every == 0:
                    self.counter = 0

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            stream_id += 1

    def draw_chicken(self, frame, results, stream_id):
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            for box, track_id in zip(boxes, track_ids):
                conf = results[0].boxes.conf.tolist()
                x1, y1, x2, y2 = box.tolist()
                pict = frame[int(y1):int(y2), int(x1):int(x2)]
                output_path = f'{self.output_path}/chicken/{stream_id}_{track_id}/{stream_id}_{track_id}_{self.video_frame_count}.jpg'
                if not os.path.exists(f"{self.output_path}/chicken/{stream_id}_{track_id}"):
                    os.makedirs(f"{self.output_path}/chicken/{stream_id}_{track_id}")
                cv2.imwrite(output_path, pict)

            return track_ids
        return None


if __name__ == '__main__':
    ChickenClipper("d:\\kurnik\\", output_path="d:\\kurnik\\").run()
