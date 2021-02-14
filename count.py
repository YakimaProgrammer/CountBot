"This program only requires minimal configuration and tweaking (xkcd.com/1742/)"
#Mostly, you'll need to use pyautogui.mouseInfo() to check how the coordinates in this program correspond to the coordinates on your screen.

import pyautogui, time, pyperclip

#all print statements can be omitted. They are just for debugging purposes

#Pyautogui tends to have occassional issues when you call a function. Calling the function again fixes things
def getpixel(x, y):
    while True:
        try:
            return pyautogui.pixel(x,y)
        except:
            pass

def getnumber():
    while True:
        try:
            #coordinates of the number in a message
            pyautogui.click(388 if side else 812, 599, clicks = 2)
            pyautogui.hotkey("ctrl","c")
            return int(pyperclip.paste())
        except ValueError:
            if pyperclip.paste() != "\r\n":
                if not pyperclip.paste().startswith(("0","1","2","3","4","5","6","7","8","9")):
                    return lastnumber
            
                                            
            
"""
SETUP:
Discord (app): right side, minimum size
Discord (webbrowser): left side, just about covering up the e in message

In the righthand Discord client, type the next number in sequence.
Run this program.
"""

#These are the RGB values that signify a count was accepted
accepted_pixels = {
    (119, 178, 85), #RGB values of the checkboxes 
    (34, 102, 153)
}

#pyautogui.PAUSE = 0 #Might cause problems depending on implementation of pixle()

#Start on the left side
side = 0

#Wait 5 seconds so you have time to set up
for i in range(5):
    print(i)
    time.sleep(1)

#This should always be zero. The program will determine what value this should be automatically
lastnumber = 0

while True:
    #Switch sides (which user is counting)
    side = not side

    while (currentnumber := getnumber() + 1) == lastnumber:
        #click the textbox so I'm on the correct side of the screen
        pyautogui.click(410 if side else 967, 679)

        #Just so I remember when the loop started so I can break out if needed
        start = time.time()
        
        while ((pixel := getpixel(404 if side else 829, 627)) not in accepted_pixels):
            #print("Got", pixel)

            if pixel == (255, 255, 255): #if I open python, stop running. The background for the python shell on my computer is white RGB(255,255,255)
                raise SystemExit

            #someone probably sent a chat message. Just to be safe, I'm going to wait 10 seconds for the last message to be verified
            #this also fires on 100, and 420, since those get a nonstandard verification reaction
            if time.time() > start + 10:
                #print("breaking out...")
                break
        else:
            #this only runs if I didn't break
            #print("fired!")
            continue
        
        #This state is only reachable if I break
        #I manually increase the count because the code that normally increases the count when the count is verified won't run when I'm in this state
        currentnumber += 1
        break

    #click in the textbox again to start writing
    pyautogui.click(410 if side else 967, 679)
    pyautogui.write(str(currentnumber))
    pyautogui.press("enter")
    #print(currentnumber)

    #remember the last number so I can check if Discord hasn't registered my message yet
    lastnumber = currentnumber

    #Now let's check if someone messed it up
    if getpixel(347, 520) == (103, 89, 207) or getpixel(774, 588) == (103, 88, 207): #coordinates and RGB values of the purple +1 countbot logo
        #Count bot is really wierd when restarting a count
        #The best way is to just spam "1" until it registers
        while ((pixel := getpixel(404 if side else 829, 627)) not in accepted_pixels):
            pyautogui.write("1")
            pyautogui.press("enter")
            time.sleep(2)

        #reset back to the starting position
        currentnumber = 1
        lastnumber = 1
