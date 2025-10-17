# capture_images.py
import cv2
import os
def create_dataset():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
    
        print("ERROR: Cannot access webcam.")
        return
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    id_input = input("Enter numeric ID for the person (e.g. 1): ").strip()
    name = input("Enter name (e.g. John Doe): ").strip().replace(" ", "_")
    if not id_input.isdigit():
        print("ID must be a number. Exiting.")
        cam.release()
        return
    dataset_path = os.path.join("dataset", f"{id_input}_{name}")
    os.makedirs(dataset_path, exist_ok=True)

    print("Starting capture. Look at the camera. Press 'q' to quit early.")
    count = 0
    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (200, 200))
            file_path = os.path.join(dataset_path, f"{count}.jpg")
            cv2.imwrite(file_path, face_img)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, f"Images Captured: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.imshow("Capturing Faces - Press 'q' to stop", img)
        k = cv2.waitKey(100) & 0xff
        if k == ord('q') or count >= 50:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"Done. {count} images saved to {dataset_path}")

if __name__ == "__main__":
    create_dataset()
