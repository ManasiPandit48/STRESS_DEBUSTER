import cv2
import numpy as np
from keras.models import model_from_json
import tkinter as tk
from tkinter import messagebox
import time
import threading
import subprocess

# Set TensorFlow to only show errors
import tensorflow as tf

tf.get_logger().setLevel('ERROR')

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("model/emotion_model.h5")
print("Loaded model from disk")

# Flag to track if stress was detected in the last interval
stress_detected_last_interval = False


# Function to run the webcam feed and stress detection
def webcam_thread():
    global stress_detected_last_interval

    # Sleep for 1 minute before starting emotion detection
    time.sleep(30)

    # start the webcam feed
    cap = cv2.VideoCapture(0)

    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        if not ret:
            break
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces available on camera
        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        # take each face available on the camera and preprocess it
        for (x, y, w, h) in num_faces:
            roi_gray_frame = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            # predict the emotions
            emotion_prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(emotion_prediction))

            # Treat Happy as Neutral, and other emotions as stress
            if maxindex == 3:
                stress_detected = False  # Happy, treat as Neutral
            else:
                stress_detected = True  # Other emotions treated as Stress

            # Check if stress is detected and it's not in the last interval
            if stress_detected and not stress_detected_last_interval:
                # Display a notification
                root = tk.Tk()
                root.withdraw()
                result = messagebox.showwarning("Stress Detected",
                                                "Stress has been detected. Take a break!!!!!")

                # Additional action for stress detection can be added here

                # Close the notification window
                root.destroy()

                # Open Main_Window.py if the user clicks OK
                if result == 'ok':
                    subprocess.Popen(["python", "Main_Window.py"])

                # Set the flag to indicate stress detection in the last interval
                stress_detected_last_interval = True

        # Check if 15 minutes have passed to reset the flag
        if time.time() % (15 * 60) < 1:
            stress_detected_last_interval = False

    cap.release()
    cv2.destroyAllWindows()


# Start the webcam thread immediately
webcam_thread = threading.Thread(target=webcam_thread)
webcam_thread.start()

# Main loop to keep the script running
while True:
    # Check if 15 minutes have passed after the last stress detection
    if time.time() % (15 * 60) < 1 and stress_detected_last_interval:
        # Display a notification for the end of the break
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Break Time Over",
                            "Your break time is over. You should get back to work now after this fantastic mood refreshment.")
        root.destroy()

    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
