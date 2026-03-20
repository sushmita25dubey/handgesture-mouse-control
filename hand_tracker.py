import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_conf=0.7, track_conf=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        return frame

    def get_landmarks(self, frame):
        h, w, _ = frame.shape
        landmarks = []

        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((id, cx, cy))

            self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)

        return landmarks