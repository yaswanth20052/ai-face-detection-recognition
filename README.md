# 🧠 AI-Based Smart Face Detection and Recognition System

## 📌 Overview
This project implements a real-time face detection and recognition system using computer vision techniques. It uses a webcam to detect human faces and recognize individuals based on a trained dataset.

The system is built using Python, OpenCV, Haar Cascade, and LBPH algorithm, and can detect multiple faces and identify known persons in real time.

---

## 🎯 Features
- Real-time face detection
- Face recognition using LBPH
- Detects multiple faces
- Displays name of person
- Shows "Unknown" for unrecognized faces
- Counts total number of faces
- Works with webcam

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- NumPy  
- Haar Cascade  
- LBPH Algorithm  

---

## 📁 Project Structure
ai-face-detection-recognition/
│
├── dataset/
├── trainer/
├── capture_dataset.py
├── train_model.py
├── face_recognition_system.py
├── README.md

---

## ⚙️ How It Works
1. Capture face images using webcam  
2. Store images in dataset folder  
3. Train model using LBPH algorithm  
4. Detect faces using Haar Cascade  
5. Recognize faces using trained model  
6. Display name and face count  

---

## ▶️ How to Run

### Install Dependencies
pip install opencv-contrib-python numpy

### Capture Dataset
python capture_dataset.py

### Train Model
python train_model.py

### Run System
python face_recognition_system.py

---

## 📊 Output
- Face detection with bounding box  
- Name display for recognized faces  
- "Unknown" label for new faces  
- Face count displayed  

---

## 🚀 Future Scope
- Emotion detection  
- Attendance system  
- Deep learning models  
- Mobile/web integration  
- Mask detection  

---

## 🎓 Applications
- Attendance systems  
- Security systems  
- Surveillance  
- Access control  

---

## 📚 References
- https://opencv.org  
- https://python.org  

---

## 👨‍💻 Authors
- A Yaswanth Kumar  

---

## ⭐ Note
Developed for the course:
Visual Recognition and Scene Understanding (23SDCS19 R/A)  
K L Deemed to be University (2025–26)
