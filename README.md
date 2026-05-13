# 🎭 Real-Time Face Gender & Emotion Detector

A real-time face analysis system that detects faces through your webcam and predicts the **gender** and **emotion** of the person using AI.

---

## 📸 Demo
- Detects faces in real time using your webcam
- Draws a green box around detected faces
- Displays gender (Man/Woman) and emotion (Happy, Sad, Angry, etc.)

---

## 🧠 How It Works
1. Webcam captures live video frames
2. OpenCV detects faces in each frame
3. DeepFace AI model analyzes the face
4. Gender and emotion are displayed on screen in real time

---

## 🛠️ Tech Stack
- **Python** — core programming language
- **OpenCV** — webcam capture and face detection
- **DeepFace** — AI-powered gender and emotion analysis
- **TensorFlow / tf-keras** — powers the DeepFace models

---

## 📁 Project Structure
---
│
├── main.py                    # Combined face box + gender + emotion detector
├── face_detection.py          # Face detection only
├── gender_emotion_detector.py # Gender and emotion detection only
├── requirements.txt           # Required libraries
└── .gitignore                 # Git ignore file

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/DanSiv246/Hackathon-Project.git
cd Hackathon-Project
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Full detector (recommended)
```bash
python main.py
```

### Face detection only
```bash
python face_detection.py
```

### Gender and emotion only
```bash
python gender_emotion_detector.py
```

> Press **Q** to quit the application

---

## 📦 Requirements
