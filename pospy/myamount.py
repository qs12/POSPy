import pyautogui, time 




processButton = (860,1020)
processButtonColor=(229,232,238) #this is the RGB color value, not location
transAmountField= (340,515)
saleRadioButton = (348,166)

amount=raw_input("Enter your amount, Ex., 12.34  ---: ")

pyautogui.click(3,3)

i=0
while i<20:
	pyautogui.click(transAmountField)
	pyautogui.hotkey('ctrl','a')
	pyautogui.typewrite(amount)
	while not pyautogui.pixelMatchesColor(processButton[0], processButton[1],processButtonColor,tolerance=8):
		time.sleep(0.5)
		#print (">>>To cancel the program, click on Command Line and press Ctrl-C<<<")
	pyautogui.click(processButton)
	if i<1:
		print ("")
	elif i==1:
		print ("You ran " +str(i)+" transaction")
	else:
		print ("You ran " +str(i)+" transactions")
	i+=1