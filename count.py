import pyautogui, time

currentnum = 3132#2104 1416
side = 0

for i in range(5):
    print(i)
    time.sleep(1)

for i in range(15000): #while True:
    currentnum += 1
    side = not side
    pyautogui.click(410 if side else 967, 679)
    [pyautogui.press(c) for c in str(currentnum)]
    pyautogui.press("enter")
    time.sleep(1.25)
