# train_model.py
import cv2
import os
import numpy as np
from PIL import Image

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    dataset_path = 'dataset'
    image_paths = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_paths.append(os.path.join(root, file))

    face_samples = []
    ids = []
    names = {}
    for image_path in image_paths:
        try:
            PIL_img = Image.open(image_path).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
        except Exception as e:
            print("Could not read image:", image_path, e)
            continue

        folder = os.path.basename(os.path.dirname(image_path))
        id_str, name = folder.split('_', 1)
        id_num = int(id_str)

        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id_num)
        names[id_num] = name

    if len(face_samples) == 0:
        print("No faces found. Please capture images first.")
        return

    recognizer.train(face_samples, np.array(ids))
    os.makedirs('trainer', exist_ok=True)
    recognizer.write('trainer/trainer.yml')
    with open('trainer/names.csv', 'w') as f:
        for id_num, name in names.items():
            f.write(f"{id_num},{name}\n")
    print("Training complete. Model saved to trainer/trainer.yml and trainer/names.csv")

if __name__ == "__main__":
    train()
