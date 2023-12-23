# VARIABLE MEANINGS
# activebtn   | The btn that is being hovered over
# activebtnobj| The activebtn ModInfo object
# tick        | The amount of times the menu has been rendered
# waitvar     | The variable being used for the wait_untill_var_0 function
# stngs       | The variable that contains all ModInfo objects
# stnginfo    | Used in the main render for loop, this variable contains the info of the current ModInfo
# is_active   | Used in the main render for loop, this variable tells the for loop if the current rendered btn is the active btn
# event       | The current keyboard event
import keyboard
from colorama import Fore, Style, Back
from Backend.mods import Mods
from Backend.classes import *
from Backend.settings import *
from os import system as cmd
from threading import Thread
from time import sleep
global activebtn
activebtn = 0
activebtnobj = None
tick=0
waitvar=1
stngs = Settings.get_settings()
def clr(): cmd("cls")
def wait_untill_var_0(var:str): # waits untill a specificed var is 0
    while not eval(f"{var}==0"): # while var isnt 0
        sleep(0.001) # blankspace

def toggle_active(): # toggles the active btn on or off
    global activebtn # makes it global for no error
    if stngs[int(activebtn)].active == False: stngs[int(activebtn)].active = True
    else: stngs[int(activebtn)].active = False          # toggles active
    if stngs[int(activebtn)].active == True: Thread(target=stngs[int(activebtn)].enable_func).start()
    else: Thread(target=stngs[int(activebtn)].disable_func).start() # runs the disable func or enable func depending on if active or not
    waitvar=0 # disables waitvar. used in rendering
def active_up(): # makes the activebtn var go up by one
    global activebtn
    if activebtn == len(stngs)-1: # checks if it cant go up 1 more
        return #                    and if so, returns
    activebtn+=1 # main purpose of this function
    waitvar=0 # disables waitvar. used in rendering
def active_down(): # almost same thing as active_up
    global activebtn
    if activebtn == 0:
        return 
    activebtn-=1
    waitvar=0 # disables waitvar. used in rendering

while True:
    clr() # clears the previous messages
    for stnginfo in stngs: # for each setting in settings
        if stnginfo.i == activebtn: is_active = True # sets is_active to true if the activebtn is the btn being rendered
        else: is_active = False                      # else, set to false
        if is_active: activebtnobj = stnginfo        # sets the activebtnobj if is_active is true
        print(f"{Back.GREEN if is_active else Back.RED}[{stnginfo.i}] {stnginfo.name}{Style.RESET_ALL}") # renders green if is_active is true else red, then renders the name and index
    print(f"Description: {activebtnobj.desc}") # renders the activebtn description
    event = keyboard.read_key() # reads for key presses
    match event:
        case "down":
            active_up() # puts active btn up
            sleep(0.2)  # waits so no spam btns
        case "up":
            active_down() # puts active btn down
            sleep(0.2)    # waits so no spam btns
        case "enter":
            toggle_active() # toggles the activebtn
            sleep(0.2)      # waits so no spam btns
        case "escape":
            quit() # doesnt work i think
    clr()
    tick+=1 # tick is used for debugging  
