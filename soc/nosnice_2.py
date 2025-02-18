import os

import cv2
import numpy as np
from ultralytics import YOLO

from reidentification.util import list_jpg_files


def apply_mask2(image, mask):
    # Convert to numpy arrays
    image = np.array(image)
    mask = np.array(mask, dtype='uint8')
    result = cv2.bitwise_and(image, image, mask=mask)
    return result


def apply_mask(image, mask):
    # Convert to numpy arrays
    image = np.array(image)
    mask = np.array(mask, dtype='uint8')

    # Ensure mask is binary (0 or 255)
    mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]

    # Create an output image with a white background
    h, w = image.shape[:2]
    result = np.ones((h, w, 3), dtype='uint8') * 255  # Start with a white image

    # Copy the original image where the mask is applied
    result[mask == 255] = image[mask == 255]

    return result

def segment_countour(input):
    model = YOLO('yolov8x-seg.pt')

    list_of_images = list_jpg_files(input, '.jpg')

    for image_path in list_of_images:
        image = cv2.imread(image_path)
        H, W, _ = image.shape
        # Perform inference
        results = model(image, task='segment')[0]

        # Extract masks and bounding boxes for 'chicken' class (often class 0 in COCO dataset)
        clss = results.boxes.cls.cpu().tolist()
        confs = results.boxes.conf.cpu().tolist()

        index = 0
        for result in results:
            if clss[index] == 14:
                if confs[index] > 0.5:
                    for j, mask in enumerate(result.masks.data):
                        mask = mask.cpu().numpy() * 255
                        mask = cv2.resize(mask, (W, H))
                        res_image = apply_mask(image, mask)
                        cv2.imwrite(image_path  +".png", res_image)
            index = index + 1


if __name__ == '__main__':
    segment_countour("d:\\kurnik\\chicken")