import pyautogui
import numpy as np
import time
from utils import distance, fingers_up

class MouseController:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.prev_x, self.prev_y = 0, 0
        self.smoothing = 0.2

        self.last_click_time = 0
        self.dragging = False

    def control(self, landmarks):
        if not landmarks:
            return

        fingers = fingers_up(landmarks)

        x1, y1 = landmarks[8][1], landmarks[8][2]  #index
        x2, y2 = landmarks[4][1], landmarks[4][2]  #thumb
        x3, y3 = landmarks[12][1], landmarks[12][2]  #middle

        #Move Cursor (Index Finger Only)
        if fingers == [0,1,0,0,0]:
            screen_x = np.interp(x1, [100, 500], [0, self.screen_w])
            screen_y = np.interp(y1, [100, 400], [0, self.screen_h])

            self.prev_x += (screen_x - self.prev_x) * self.smoothing
            self.prev_y += (screen_y - self.prev_y) * self.smoothing

            pyautogui.moveTo(self.prev_x, self.prev_y)

        #Left Click (Thumb + Index)
        if distance((x1,y1),(x2,y2)) < 30:
            if time.time() - self.last_click_time > 0.5:
                pyautogui.click()
                self.last_click_time = time.time()

        #Right Click (Thumb + Middle)
        if distance((x3,y3),(x2,y2)) < 30:
            pyautogui.rightClick()

        #Scroll (Two Fingers)
        if fingers == [0,1,1,0,0]:
            pyautogui.scroll(30 if y1 < self.prev_y else -30)

        #Drag & Drop
        if distance((x1,y1),(x2,y2)) < 20:
            if not self.dragging:
                pyautogui.mouseDown()
                self.dragging = True
        else:
            if self.dragging:
                pyautogui.mouseUp()
                self.dragging = False