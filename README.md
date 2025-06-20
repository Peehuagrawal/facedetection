# 😊 Face Detection Module (MediaPipe + OpenCV)

A lightweight, reusable Python module for detecting faces in real-time video streams or images using **MediaPipe** and **OpenCV**.

This project serves as a solid base for any face-related application — from smart attendance systems to facial emotion recognition. Easily pluggable into larger computer vision pipelines!

---

## ✨ Why This Module?

✔️ Minimal code, easy to understand  
✔️ Modular: built for reusability  
✔️ Accurate face bounding using MediaPipe's Face Detection model  
✔️ No deep learning setup or training required  
✔️ Great for beginners and rapid prototyping

---

## 🛠️ Technologies Used

| Tool        | Role                                |
|-------------|-------------------------------------|
| Python      | Programming language                |
| OpenCV      | Camera stream & drawing utilities   |
| MediaPipe   | Fast and lightweight face detection |

---

## 📂 Project Structure

```
facedetection/
│
├── FaceDetectionModule.py   # Core face detection logic
├── main.py                  # Example usage script
├── requirements.txt         # Required packages
└── README.md                # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Peehuagrawal/facedetection.git
cd facedetection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Example

```bash
python facedetectionmodule.py
```

> Make sure your webcam is connected and accessible.

---

## 🧠 How to Use the Module

You can import and use the `FaceDetector` class in your own projects:

```python
from FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.75)

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    cv2.imshow("Face Detection", img)
    cv2.waitKey(1)
```

---

## ⚙️ Customization Options

The `FaceDetector` class accepts the following parameter:

- `minDetectionCon`: *(float)* — Minimum detection confidence (default is `0.5`). Increase it to reduce false positives.

---

## 🌟 Potential Use Cases

- Face recognition systems  
- Emotion detection  
- Auto-focus camera features  
- Digital mirror or beauty filters  
- Smart classroom/attendance tracking  
- Face-based authentication

---

## 🧩 Future Extensions

- Add face landmarks (eyes, nose, mouth)
- Integrate with facial recognition models
- Enable multiple face tracking
- Add video recording and face blur features

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 🙋‍♀️ Author

**Peehu Agrawal**  
📎 [GitHub](https://github.com/Peehuagrawal)

---

> 💡 *Fork this repo to kickstart your own face-based vision project. PRs and ideas are welcome!*

