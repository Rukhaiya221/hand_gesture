1. Project Overview

This project is a Hand Gesture Controlled Game Controller built using Python, OpenCV, MediaPipe, and PyAutoGUI.

The system detects hand gestures through a webcam and converts them into keyboard actions for controlling games such as:

Subway Surfers
Temple Run
Browser Games
Simple PC Games
2. Features

✅ Real-time hand tracking
✅ Gesture-based controls
✅ Uses webcam input
✅ Fast response system
✅ Simple and lightweight

3. Supported Gestures
Gesture	Action	Keyboard Key
Hand Right	Move Right	Right Arrow
Hand Left	Move Left	Left Arrow
Hand Up	Jump	Up Arrow
Hand Down	Roll / Slide	Down Arrow
Fist ✊	Pause Game	P
🛠️ Technologies Used
Python
OpenCV
MediaPipe
PyAutoGUI
4.  Project Structure
gesture-controller/
│
├── main.py
├── README.md
└── requirements.txt
5. installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/gesture-controller.git
2️⃣ Open Project Folder
cd gesture-controller
3️⃣ Install Dependencies
pip install opencv-python mediapipe pyautogui

OR

pip install -r requirements.txt
▶️ Run the Project
python main.py
6. How It Works
Webcam captures live video.
MediaPipe detects hand landmarks.
Program calculates hand direction.
Corresponding keyboard key is triggered using PyAutoGUI.
Game responds to gestures in real time.
