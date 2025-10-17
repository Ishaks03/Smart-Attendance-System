# recognize.py
import cv2
import os
import csv
from datetime import datetime

def load_names():
    names = {}
    path = 'trainer/names.csv'
    if os.path.exists(path):
        with open(path, 'r') as f:
            for line in f:
                parts = line.strip().split(',', 1)
                if len(parts) == 2:
                    names[int(parts[0])] = parts[1]
    return names

def mark_attendance(id_num, name):
    filename = 'attendance.csv'
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID','Name','Date','Time'])
    # check duplicate for same date
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'] == str(id_num) and row['Date'] == date_str:
                return
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_num, name, date_str, time_str])
    print(f"Attendance marked: {id_num}, {name}, {date_str} {time_str}")

def recognize():
    if not os.path.exists('trainer/trainer.yml'):
        print("Model not found. Train first with train_model.py")
        return
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    names = load_names()
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("ERROR: Cannot access webcam.")
        return

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            try:
                id_num, confidence = recognizer.predict(roi)
            except Exception as e:
                # sometimes faces too small or model issues
                id_num, confidence = -1, 1000
            if confidence < 70:  # lower is better; adjust threshold as needed
                name = names.get(id_num, "Unknown")
                cv2.putText(img, f"{name}", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                mark_attendance(id_num, name)
            else:
                cv2.putText(img, "Unknown", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow('Attendance - Press ESC to exit', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27:  # ESC key
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize()
