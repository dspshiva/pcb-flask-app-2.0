from ultralytics import YOLO
import cv2

# Load the YOLO model (replace with your .pt path)
model = YOLO("best.pt")  # put correct name of your .pt file

def detect_image(image_path):
    # Run inference
    results = model(image_path)[0]

    # Plot results on the image
    annotated_frame = results.plot()

    return annotated_frame
