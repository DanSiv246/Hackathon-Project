import os
from pathlib import Path

os.environ.setdefault("DEEPFACE_HOME", str(Path(__file__).resolve().parent))

import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

# Store last result
gender = ""
emotion = ""
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        faces = [max(faces, key=lambda f: f[2] * f[3])]

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Only analyze every 5th frame
    if frame_count % 2 == 0:
        try:
            result = DeepFace.analyze(
                frame, actions=["gender", "emotion"], enforce_detection=False
            )
            gender = result[0]["dominant_gender"]
            emotion = result[0]["dominant_emotion"]
        except:
            pass

    # Always show last known result
    cv2.putText(
        frame,
        f"{gender}, {emotion}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    frame_count += 1

    cv2.imshow("Face Analyzer", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
