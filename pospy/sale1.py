"""This is a Stress simulation program that utilizes python GUI automation modules. 
Make sure your POS simulator takes exactly half of left side of the screen (to achieve that,
 press POS simulator and hit "Windows key+left arrow"), and do not move POS simulator window!


Sale2.py automates Sales commands with automatically filled amounts of $5, $25, $50, $75, 
$100, $125, $200, $500, $800,$1100, and $1400 sent one after another. These sale commands are 
performed back-to-back, so that user doesn't have to fill in abovementioned amounts manually.
This program is useful for:
1. Boundary testing (i.e. CVM Limits, CTLS CVM Limits, etc)
2. Testing every card brand with different amounts.


To stop this program, click on cmd.exe (or Command Prompt) and hit Ctrl-C. 
Dragging mouse to upper-left corner of the screen might not work for this program.
"""
import pyautogui, time 



processButton = (860,1020)
processButtonColor=(229,232,238) #this is the RGB color value, not location
transAmountField= (340,515)
saleRadioButton = (348,166)

"""All above variables (like "processButton") are assigned to certain location on the screen.
If elements on your screen are located somewhere different, then do following:
1. Make Command Line window active
2. Place your cursor/mouse tick on the element you need (do not click on it!!)
2. With Command line still active, navigate to 'py' (if not already there)
3. Type 'python position.py'
4. In the Command line, you will get exact x/y coordinates
5. Substitute your exact coordinates with old value
"""

pyautogui.click(3,3)
pyautogui.click(saleRadioButton)
pyautogui.click(transAmountField)
pyautogui.hotkey('ctrl','a')
pyautogui.typewrite('5.00')
pyautogui.click(processButton)

i=25
n=300
while i<150:
	pyautogui.click(transAmountField)
	pyautogui.hotkey('ctrl','a')
	pyautogui.typewrite(str(i) +'.00')
	while not pyautogui.pixelMatchesColor(processButton[0], processButton[1],processButtonColor,tolerance=8):
		time.sleep(0.5)
		#print (">>>To cancel the program, click on Command Line and press Ctrl-C<<<")
	pyautogui.click(processButton)
	i+=25
i=200
while i <1500:
	pyautogui.click(transAmountField)
	pyautogui.hotkey('ctrl','a')
	pyautogui.typewrite(str(i) +'.00')
	while not pyautogui.pixelMatchesColor(processButton[0], processButton[1],processButtonColor,tolerance=8):
		time.sleep(0.5)
		#print (">>>To cancel the program, click on Command Line and press Ctrl-C<<<")
	pyautogui.click(processButton)
	i+=300

