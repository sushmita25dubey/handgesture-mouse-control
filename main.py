import cv2
import time
import pyautogui
from hand_tracker import HandTracker
from mouse_controller import MouseController

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

tracker = HandTracker()
screen_w, screen_h = pyautogui.size()
controller = MouseController(screen_w, screen_h)

prev_time = 0

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    tracker.find_hands(frame)
    landmarks = tracker.get_landmarks(frame)

    controller.control(landmarks)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(frame, f"FPS: {int(fps)}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("Gesture Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()