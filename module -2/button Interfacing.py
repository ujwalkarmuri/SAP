
# Example for using the Grove Button 

import time
import grovepi

# Connect the Grove Button to digital port D3
button = 3

grovepi.pinMode(button,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)

    except IOError:
        print ("Error")