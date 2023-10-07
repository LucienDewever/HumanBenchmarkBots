from PIL import Image, ImageGrab
import keyboard
import pyautogui


def createCoordinate():
    placeholder =None




xval = 980
yval = 580
coordinate = (980,580)





def main():
    
    gameplay(coordinate)
 

def gameplay(coordinate):
    while True:
        if keyboard.is_pressed('q'):
            break
        screen = ImageGrab.grab()
        color = screen.getpixel(coordinate)
        if color == (126, 214, 119):
            pyautogui.click(xval,yval)
        
        
main()