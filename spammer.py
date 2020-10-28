import pyautogui
import time

with open("./Source.txt", "r") as Lyrics:
    input("Press enter to start")
    print("Starting in 3 seconds.")
    time.sleep(3)
    for line in Lyrics.readlines():
        try:
            time.sleep(1)
        except:
            input("Froze... Press Ctr+C again to close")
        print(f"Writting: \"{line.strip()}\"")
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')
time.sleep(3)