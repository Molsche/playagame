import pyautogui
import time

def get_mouse_location():
    print("Bewege die Maus über die gewünschte Ecke...")
    time.sleep(2)  # Gib dir Zeit

    position = pyautogui.position()
    print(f"Aktuelle Mausposition: {position}")