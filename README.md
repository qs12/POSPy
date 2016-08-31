# POSPy

POSPy  - v 1.0
GUI Automation tool for POS simulator.








Table of Content:

1. Overview ----------------------------------------------------p.2
2. Workstation setup ----------------------------------------p.3
3. Running programs ------------------------------------p.4
4. Programs description --------------------------------p. 
4. Debugging ----------------------------------p.5






































Overview:

POSPy  is a set of programs - or at least a working attempt - to alleviate the pain that comes with testing SCA commands manually.

POSPy  utilizes GUI automation Python module called PyAutoGUI, which used to programmatically control the mouse & keyboard.

The program requires a fixed position of the POS simulator on the screen, as all saved variables are assigned to fixed position on x,y coordinate system. x and y axis start on the upper left corner (0,0) and end at lower right corner (Ex., 1920,1080).

 



































Workstation setup:


In order to use POS-Automation tool you need to setup your system beforehand. That includes following steps below:
1.	Installing python 2.7 (If you have python on your system, you may skip this section)
1.1	Go to https://www.python.org/downloads/ and download the latest 2.7 version for Windows. Do not download Python 3 version!

1.2	Run the installer;
On Customize screen, scroll down in the window and find the “Add Python.exe to Path” and click on the small red “x.” Choose the “Will be installed on local hard drive” option then press “Next.”
 

1.3	After python is installed, we need to add Python to System Path Variable. In order to do that, Click on Windows emblem and type ‘environment’ – choose “Edit the system environment variables”
When the “System Properties” window appears, click on “Environment Variables…”

 

When the “System Properties” window appears, click on “Environment Variables…”: 
 

Once you have the “Environment Variables” window open, direct your focus to the bottom half. You will notice that it controls all the “System Variables” rather than just this associated with your user. Click on “New…” to create a new variable for Python.

 

Simply enter a name for your Path and the code shown below. For the purposes of this example we have installed Python 2.7.3, so we will call the path: “Pythonpath.”
The string that you will need to enter is: “C:\Python27\;C:\Python27\Scripts;”
 

Press “OK,” then “OK,” then “OK,” then the red “X” to accept all changes and exit the “System Properties” window.


1.2  Check that you’ve installed python successfully. Open ‘cmd’ or Command Prompt and type python. You should see something similar to this. If you getting error message, try repeating step 1.2
 


To exit from python scripting mode in cmd, type quit() and press enter:


2. Installing pyautogui and its dependencies:
2.1  Install Pillow
In Command Prompt, navigate to C:\Python27\Scripts and type easy_install pillow


2.3 Install PyAutoGUI
 Once pillow installed, type pip install pyautogui


2.4 Check installation
Once pyautogui installed, type pip list (or pip freeze) to check whether all needed packages are installed:


Seems like everything is installed, so we can move to the next step now.

3. Locating your programs.

3.1 Placing pospy folder

As you noticed, whenever you open a Command line, the path is always pointing to your user directory:
 

Place your extracted pospy folder inside your user directory (it will save you from endless navigation):

 




	3.2 Navigate to pospy folder in cmd:

Type cd pospy to go inside the folder:

 

Great! You’re in the right working directory! You can now launch the programs.








Running programs


In order to run your programs, you need:
1.	Pair POS-simulator to your terminal and start a session. (For error-free results please use the pos-simulator provided along with POSPy. If you for any reason need to use different version of POS-simulator, and POSPy  programs don’t seem to work properly, please refer to Debugging section)
2.	While POS-simulator window is active, press “  + ←" (Windows logo key+left arrow) shortcut. This will allow POS simulator to take exactly half of the left screen of user's monitor. 
 

3.	Navigate to pospy folder in cmd (See section 3.2)
4.	In cmd, type python sale.py to run sales.py program. Same goes for any other program – type ‘python program_name.py’
 
That’s it! POSPy is now running!
5.	To stop your program, you need to click on cmd and press “Ctrl-C”.. If that didn’t stop your program, drag your mouse to the upper-left corner.
 If above two options still couldn’t stop you program - log out, or press “  - L” .
Programs description

1.	Lineitem.py:
Sends 100 line items to the terminal one by one.
2.	Sale.py:
Sends 25 CAPTURE commands with $1.00. Cmd will count number of transactions you performed.
Sale1.py:
Sends $5, $25, $50, $75, $100, $125, $200, $500, $800, $1100, and $1400 CAPTURE commands one after another. 
3.	Sale2.py:
Sends CAPTURE commands starting with $1.00, and then it increments with $1.00 for every next transaction. It stops at $150.00.  Ex., $1.00, $2.00, $3.00 … $150.00. 
Cmd will count number of transactions you performed.
4.	Myamount.py
Cmd will prompt you to enter the amount you want to run:
 
Enter your amount and press enter. The program will run 20 CAPTURE commands with given amount. Cmd will count number of transactions you performed.
 
5.	Position.py:
Determines current mouse location on the screen
6.	Screensize.py:
Determines screen resolution (Ex., 1920x1080)
7.	Getcolor.py:
Determines the color of a certain pixel. You need to provide the pixel location in the file:
 











Debugging:

1.	POSPy not running
One of the first things to look at is whether your POS-simulator obstructed by other programs/applications or not.
Make sure your POS-simulator is not FULLY obstructed by other programs/applications when you are to run your programs. POSPy simulates mouse on screen and you need to allow at least a small visible part of POS-simulator on the uttermost left side of the screen when running POSPy programs:
Below example is acceptable:

 


2.	Finding Mouse Location on Screen
If your mouse clicks are off the target or you’ve decided to use the right side of the screen to place POS-simulator, you can easily overcome this obstacle by figuring out your mouse/cursor location on the screen and overwriting variables inside each program with new values.

To find exact position of you mouse, do the following:
1. Make Command Line window active
2. Place your cursor/mouse tick on the element you need (do not click on it!!)
2. With Command line window still active, navigate to 'py' (if not already there)
3. Type python position.py
In the Command line, you will get exact x/y coordinates:
 
5. Replace old coordinates with your exact new values:
	a. open a program/file you need to edit in Text Editor (I use Sublime);
	b. Find variables on top of each file that are self-explanatory:
 
	c. Replace with new values and save.
6. Now Test the program.



