import time
from random import randrange
import pyautogui
q = True
z = "go" 
print("launching")

time.sleep(2)
if z == input("mdp? "):
	print("a vos kamas")
	try:
		while q:
			pyautogui.moveTo(x=1199, y=325, duration=0.5)
			time.sleep(0.1)
			pyautogui.click(button='right')
			time.sleep(0.1)
			pyautogui.moveTo(x=706, y=492, duration=0.5)
			time.sleep(0.1)
			pyautogui.click(button='left')
			time.sleep(0.1)
			pyautogui.moveTo(x=659, y=514, duration=0.5)
			time.sleep(0.1)
			pyautogui.click(button='left')
			time.sleep(0.1)
			pyautogui.moveTo(x=572, y=438, duration=0.5)
			time.sleep(0.1)
			pyautogui.click(button='left')
			time.sleep(12)
	except KeyboardInterrupt:
		print('Script fini')
else:
	print("mauvais mot")