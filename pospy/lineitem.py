import pyautogui, time

pyautogui.click(3,3)

addLineItemTic=(270,132)
FillLineItemID = (280,450)
description = (300,550)
processButton = (860,1020)
 
"""i=1
while i<100:
	pyautogui.click(270,132)
	pyautogui.click(280,450)
	pyautogui.press('backspace')
	pyautogui.typewrite(str(i))
	pyautogui.click(300,550)
	pyautogui.typewrite(' #' +str(i))
	pyautogui.click(860,1020)
	i+=1
#for i in range (100):
#	i=1
#	pyautogui.click(270,132)"""

i=1
while i<101:
	pyautogui.click(addLineItemTic)
	pyautogui.click(FillLineItemID)
	pyautogui.press('backspace')
	pyautogui.typewrite(str(i))
	pyautogui.click(description)
	pyautogui.hotkey('ctrl','a')
	pyautogui.typewrite('Item #' + str(i))
	pyautogui.click(processButton)
	i+=1