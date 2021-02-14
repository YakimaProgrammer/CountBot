import pyautogui, time, pyperclip


def getpixel(x, y):
    while True:
        try:
            return pyautogui.pixel(x,y)
        except:
            pass

def getnumber():
    while True:
        try:
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
accepted_pixels = {
    (119, 178, 85),
    (34, 102, 153) #check this number
}
#pyautogui.PAUSE = 0 #Might cause problems depending on implementation of pixle()

side = 0

for i in range(5):
    print(i)
    time.sleep(1)

lastnumber = 0

while True:
    side = not side

    while (currentnumber := getnumber() + 1) == lastnumber:
        #click the textbox so I'm on the correct side of the screen
        pyautogui.click(410 if side else 967, 679)

        start = time.time()
        
        while ((pixel := getpixel(404 if side else 829, 627)) not in accepted_pixels):
            print("Got", pixel)

            if pixel == (255, 255, 255): #if I open python, stop running
                raise SystemExit

            #someone probably sent a chat message. Just to be safe, I'm going to wait 10 seconds for the last message to be verified
            #this also fires on 100, and 420, since those get a nonstandard verification reaction
            if time.time() > start + 10:
                print("breaking out...")
                #break
        else:
            print("fired!")
           # break

    #click in the textbox to start writing
    pyautogui.click(410 if side else 967, 679)
    pyautogui.write(str(currentnumber))
    pyautogui.press("enter")
    print(currentnumber)

    lastnumber = currentnumber
    
