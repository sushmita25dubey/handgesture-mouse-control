# 🖱️ Hand Gesture Controlled Virtual Mouse

Control your computer mouse using hand gestures in real-time with the help of computer vision — no physical mouse required.


## 🚀 Overview

This project uses **OpenCV** and **MediaPipe** to track hand movements through a webcam and convert them into mouse actions like cursor movement, clicking, scrolling, and dragging.

It demonstrates a **touchless human-computer interaction system** that can be used in accessibility tools, smart environments, and futuristic interfaces.

## ✨ Features

* 🖐️ Real-time hand tracking using MediaPipe
* 🖱️ Smooth cursor movement (Index finger)
* 👆 Left click (Thumb + Index pinch)
* 👉 Right click (Thumb + Middle pinch)
* 🔽 Scroll (Index + Middle fingers)
* 🟡 Drag & Drop (Pinch hold)
* ⚡ FPS counter for performance monitoring
* 🎯 Optimized for real-time usage

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

## 📁 Project Structure
```
gesture-virtual-mouse/
│
├── main.py                # Main execution file
├── hand_tracker.py        # Hand detection & landmarks
├── mouse_controller.py    # Gesture → mouse control
├── utils.py               # Helper functions      
└── README.md
```

## ▶️ Run the Project

```bash
python main.py
```


## 🎮 Gesture Controls
| Gesture               | Action      |
| --------------------- | ----------- |
| Index Finger Up       | Move Cursor |
| Thumb + Index (Pinch) | Left Click  |
| Thumb + Middle        | Right Click |
| Index + Middle        | Scroll      |
| Pinch Hold            | Drag & Drop |

## 📊 FPS Counter
The FPS (Frames Per Second) counter shows how fast the system processes video frames.
Higher FPS = smoother and faster performance.

## 🧠 How It Works
1. Webcam captures live video
2. MediaPipe detects 21 hand landmarks
3. Finger positions are analyzed
4. Gestures are recognized
5. PyAutoGUI converts gestures into mouse actions
   
## 📸 Demo
> www.linkedin.com/in/sushmitadubey

## 🔮 Future Improvements
* 🎛️ Sensitivity & calibration settings
* 🧠 Custom gesture recognition (AI/ML)
* 🖥️ Multi-monitor support
* 🎮 Game control integration
  

## 💡 Use Cases

* Accessibility tools
* Touchless interfaces
* Smart presentations
* Gesture-based control systems

## 👩‍💻 Author
**Sushmita Dubey**
B.Tech CSE | AI & Web Development 

## ⭐ Support
If you found this project useful, please give it a ⭐ on GitHub!

---
