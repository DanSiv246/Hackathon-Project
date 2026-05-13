import cv2
from deepface import DeepFace

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    try:
        # Analyze face
        result = DeepFace.analyze(
            frame,
            actions=['gender', 'emotion'],
            enforce_detection=False
        )

        # Get data
        gender = result[0]['dominant_gender']
        emotion = result[0]['dominant_emotion']

        # Display text
        text = f"{gender}, {emotion}"

        cv2.putText(
            frame,
            text,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    except Exception as e:
        print(e)

    # Show video
    cv2.imshow("Gender and Emotion Detector", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()