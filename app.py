from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
import uuid
import cv2
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from detect import detect_image  # your YOLOv8 detection logic

load_dotenv() 

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# MySQL connection configuration using PyMySQL
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password=os.getenv('MYSQL_PASSWORD'),
        database='pcb_db',
        cursorclass=pymysql.cursors.DictCursor
    )

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    success_message = session.pop("register_success", None)

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
        connection.close()

        if not user:
            return render_template("login.html", error="❌ User not found. Please register first.")

        if not check_password_hash(user["password"], password):
            return render_template("login.html", error="❌ Incorrect password.")

        session["user"] = username
        return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("register.html", error="❌ Passwords do not match.")

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                connection.close()
                return render_template("register.html", error="❌ Username already exists.")

            hashed_password = generate_password_hash(password)
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            connection.commit()
        connection.close()

        return render_template("register.html", success="✅ Registration successful! You can now log in.")
    return render_template("register.html")

@app.route("/detect", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        image = request.files["image"]
        filename = f"{uuid.uuid4().hex}.jpg"
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(upload_path)

        # Call YOLO model
        result_img = detect_image(upload_path)

        output_filename = f"detected_{filename}"
        full_output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        relative_output_path = f"outputs/{output_filename}"

        # Save annotated image
        cv2.imwrite(full_output_path, result_img)

        session["result_img"] = relative_output_path
        return redirect(url_for("result"))

    return render_template("index.html", result_img=None)

@app.route("/result")
def result():
    if "user" not in session or "result_img" not in session:
        return redirect(url_for("login"))
    
    result_img = session.get("result_img")
    return render_template("result.html", result_img=result_img)

@app.route("/logout")
def logout():
    session.pop("user", None)
    session["logout_msg"] = "👋 You have been logged out."
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
