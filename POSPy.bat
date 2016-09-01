@echo off
title Automate POS simulator

COLOR 2F

:MENU
ECHO POSPy v1.0
ECHO.
ECHO ...............................................
ECHO.
ECHO Make sure your POS is placed EXACTLY on the right side of the screen.
ECHO To achive that, click on pos-sim and press 'Windows logo + RIGHT ARROW'
ECHO.
ECHO ...............................................
ECHO.
ECHO   Choose from menu options below:
ECHO.
ECHO  1 - Send 100 line items
ECHO  2 - $1 SALE Commands (25 times)
ECHO  3 - $1 increment SALE commands ($1 - $151)
ECHO  4 - CVM Limits ($5, $25, $50, $75, $100, $125, $200, $500, $800, $1100, $1400)
ECHO  5 - CUSTOM AMOUNT (repeats 20 times)
ECHO.

SET /P M=Type 1, 2, 3, 4 or 5 and then press ENTER:
IF %M%==1 GOTO LIneItem
IF %M%==2 GOTO SALE
IF %M%==3 GOTO INCREMENT
IF %M%==4 GOTO CVM
IF %M%==5 GOTO CUSTOM

:SALE
python C:\Users\t_semens1\POSPy\sale.py %*

GOTO MENU

:LIneItem
python C:\Users\t_semens1\POSPy\lineitem.py %*
GOTO MENU

:INCREMENT
python C:\Users\t_semens1\POSPy\sale2.py %*

:CVM
python C:\Users\t_semens1\POSPy\sale1.py %*
GOTO MENU

:CUSTOM
python C:\Users\t_semens1\POSPy\myamount.py %*
GOTO MENU


pause