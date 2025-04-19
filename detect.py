from ultralytics import YOLO
import cv2

model = YOLO("best.pt")  # Ensure 'best.pt' is in your project folder

def detect_image(image_path):
    results = model(image_path)[0]
    annotated_frame = results.plot()  # Returns a NumPy image
    return annotated_frame
