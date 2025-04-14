from flask import Flask, render_template, request
import os
import uuid
import cv2
from detect import detect_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        filename = f"{uuid.uuid4().hex}.jpg"

        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(upload_path)

        # Detect and save
        result_img = detect_image(upload_path)
        relative_output_path = f"outputs/detected_{filename}"  # for HTML
        full_output_path = os.path.join(OUTPUT_FOLDER, f"detected_{filename}")
        cv2.imwrite(full_output_path, result_img)

        return render_template("index.html", result_img=relative_output_path)

    return render_template("index.html", result_img=None)

if __name__ == "__main__":
    app.run(debug=True)
