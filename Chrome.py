import pyautogui 
import time
from PIL import Image, ImageGrab 

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data ):
    # Draw the rectangle for birds
    for i in range(200 , 300):
        for j in range(325 , 375) :

            # the black and white pixels value may be changed according to the cactus colour
            if 150 < data[i, j] < 170 :
                hit("down")
                return
            
                
    for i in range(200 , 400 + int((time2 - time1)/1.4)):
        for j in range(375 , 450):
            if 150 < data[i, j] < 170 :
                hit("up")
                return
                
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    time1 = time.time()
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        time2 = time.time()
        isCollide(data )



      
