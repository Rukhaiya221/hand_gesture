import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_action = 0
last_gesture = None

def is_fist(hand_landmarks):
    tips = [8,12,16,20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y:
            return False
    return True


while True:

    success, img = cap.read()
    img = cv2.flip(img,1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[8]
            wrist = hand_landmarks.landmark[0]

            dx = index_tip.x - wrist.x
            dy = index_tip.y - wrist.y

            current_time = time.time()

            if current_time - last_action > 0.25:

                gesture = None

                # FIST → PAUSE
                if is_fist(hand_landmarks):
                    gesture = "PAUSE"

                # RIGHT
                elif dx > 0.25:
                    gesture = "RIGHT"

                # LEFT
                elif dx < -0.25:
                    gesture = "LEFT"

                # JUMP
                elif dy < -0.25:
                    gesture = "JUMP"

                # ROLL
                elif dy > 0.25:
                    gesture = "ROLL"

                if gesture != last_gesture:

                    if gesture == "RIGHT":
                        pyautogui.press("right")
                        print("RIGHT 🫱")

                    elif gesture == "LEFT":
                        pyautogui.press("left")
                        print("LEFT 🫲")

                    elif gesture == "JUMP":
                        pyautogui.press("up")
                        print("JUMP 👆")

                    elif gesture == "ROLL":
                        pyautogui.press("down")
                        print("ROLL 👇")

                    elif gesture == "PAUSE":
                        pyautogui.press("p")
                        print("PAUSE ✊")

                    last_gesture = gesture
                    last_action = current_time

    cv2.imshow("Gesture Controller", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()