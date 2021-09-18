import pyautogui
import time

time.sleep(4)

file = open("texto.txt", "r", encoding="UTF-8")

for palavra in file:
    pyautogui.typewrite(palavra)
    pyautogui.press("enter")