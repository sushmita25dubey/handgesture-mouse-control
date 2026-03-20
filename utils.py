import math

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def fingers_up(landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    #Thumb
    fingers.append(1 if landmarks[4][1] < landmarks[3][1] else 0)

    #Other fingers
    for tip in tips[1:]:
        fingers.append(1 if landmarks[tip][2] < landmarks[tip - 2][2] else 0)

    return fingers