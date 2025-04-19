# PCB Version 2.0 - Real-Time Defect Detection for Printed Circuit Boards (PCBs)

**PCB Version 2.0** is a machine learning-based project designed to detect defects in Printed Circuit Boards (PCBs) using the YOLOv8 object detection model. This system allows real-time, high-precision identification of common PCB defects such as missing holes, mouse bites, open circuits, shorts, spurs, and spurious copper.

The project is built using **Flask** for the web interface, **YOLOv8** for defect detection, and **MySQL** for defect data storage and user authentication.

## Features

- Real-time defect detection of PCBs using YOLOv8.
- Support for detecting multiple types of defects:  
  `missing_hole`, `mouse_bite`, `open_circuit`, `short`, `spur`, and `spurious_copper`.
- Web-based interface built with Flask, allowing easy upload of images for analysis.
- Model inference using the trained YOLOv8 model (`best.pt`).
- User authentication system powered by MySQL and PyMySQL.
- Simple and scalable deployment.

## Technologies Used

- **YOLOv8** (You Only Look Once) for object detection.
- **Flask** for the web interface.
- **MySQL** for defect data storage and user authentication.
- **OpenCV** for image processing.
- **PyMySQL** for database interaction.
- **Python** for backend development.
- **TensorFlow** (optional, depending on specific implementation).

## Model Training

The YOLOv8 model was trained on a custom dataset from **Roboflow** with over 10,000 labeled PCB images. The model was trained for the following defect classes:

- `missing_hole`
- `mouse_bite`
- `open_circuit`
- `short`
- `spur`
- `spurious_copper`

The model achieves high precision and recall in identifying these defects and can be easily fine-tuned for additional defect types or better accuracy.

## Usage

1. Upload a PCB image through the web interface.
2. The system will process the image and use the YOLOv8 model to detect defects in real-time.
3. The detected defects will be displayed on the image, and defect details will be stored in the MySQL database.
4. Users can sign in via the authentication system to track previous defect analysis results.

## Images

### 1. **Demo Screenshot**  
   ![Demo Screenshot](https://github.com/dspshiva/pcb-flask-app-2.0/blob/main/static/Screenshot%202025-04-19%20150850.png)  
   A visual of the PCB image being uploaded and analyzed through the web interface.

### 2. **Model Output 1**  
   ![Model Output 1](https://github.com/dspshiva/pcb-flask-app-2.0/blob/main/static/Screenshot%202025-04-19%20150649.png)  
   An example of detected defects on a PCB image, highlighting the bounding boxes and defect labels.

### 3. **Model Output 2**  
   ![Model Output 2](https://github.com/dspshiva/pcb-flask-app-2.0/blob/main/static/Screenshot%202025-04-19%20145653.png)  
   Another example of model detection, with clear defect highlights.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to your fork (`git push origin feature-branch`).
5. Create a pull request.


## Acknowledgements

- The YOLOv8 model and **Ultralytics** for their work on the YOLO framework.
- **Flask** for providing a lightweight framework for the web interface.
- **Roboflow** for the dataset preparation and labeling tools.
- **MySQL** and **PyMySQL** for data management and authentication.
