import cv2
import numpy as np
import pyautogui
import time

region = (2382, 302, 10, 10)


def play_dino():
    print("Du hast 5 Sekunden Zeit das korrekte Fenster zu öffnen")
    for i in range(5, 0, -1):
        print(f"Starte in {i}...")
        time.sleep(1)
    print("Starte Erkennung...")

    while True:
        screenshot = pyautogui.screenshot(region=region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Is pixelcluster gray?
        print(np.mean(gray))
        if np.mean(gray) < 200:
            pyautogui.press("space")

        cv2.imshow("Game View", gray)

        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()