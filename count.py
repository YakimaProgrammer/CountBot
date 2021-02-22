#TODO: remove busy loops that just check a condition constantly
import pyautogui, time, pyperclip, collections

#You need two discord clients to do this. I'm going to make a class that reflects how the Y cordinate usually stays the same
Point = collections.namedtuple("MirroredPoint",("xleft","xright","y"))

#Now, let's make some user-specific constants
if not pyautogui.size() == (1366, 768):
    raise ValueError("You probably forgot to adjust the coordinates to match your device. Make sure you update the 'if not pyautogui.size() == (1366, 768):' line too!")

#Coordinates of various points of interest
#                  xleft  xright y
TEXTBOX =       Point(410, 967, 679)
VERIFIED =      Point(404, 829, 627)
COUNTING_LOGO = Point(347, 774, 520)
MESSAGE =       Point(388, 812, 599)  

#The pixel values to watch for
RGB_GREEN = (119, 178, 85)
RGB_BLUE = (34, 102, 153)

#Define a variable so I know what side to click on!
side = not "right" #Really, this can have any truthy or falsy value. I perfer to start on the left, hence the 'not "right"' statement.

#... and another variable to track what the last number was
lastnumber = 0

#With that out of the way, let's define some functions!
def getpixel(x, y):
    while True:
        try:
            return pyautogui.pixel(x,y)
        except:
            pass #Occassionally, pyautogui's backend will have issues. Calling the function again is enough to fix it.

def verify_count(timeout = 10):
    start = time.time()
    while time.time() < start + timeout:
        currentpixel = getpixel(VERIFIED.xleft if side else VERIFIED.xright, VERIFIED.y)
        if currentpixel == RGB_GREEN or currentpixel == RGB_BLUE:
            return True

    return False

def getnumber():
    while True:
        if verify_count():
            #coordinates of the number in a message
            pyautogui.click(MESSAGE.xleft if side else MESSAGE.xright, MESSAGE.y, clicks = 2)
            pyautogui.hotkey("ctrl","c")

            justcounted = pyperclip.paste()
            if re.match("^[1-9]\d*$",justcounted): #matches a number that doesn't start with a zero
                justcounted = int(justcounted) #this is safe because I know justcounted is an integer
                if justcounted >= lastnumber:
                    return justcounted

        return lastnumber + 1

    
for i in range(5):
    print(i)
    time.sleep(1)

while True:
    side = not side #switch sides

    #switch to the current window
    pyautogui.click(TEXTBOX.xleft if side else TEXTBOX.xright, TEXTBOX.y)

    #Type the next number
    pyautogui.write(getnumber() + 1)

    #Submit!
    pyautogui.press("enter")

    raise Exception("Still need to check if the count was valid! (Did someone mess it up?)"
