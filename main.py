import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui
Next we establish connection with the Arduino through COM port. In my computer the Arduino
is connected to COM 18. Use device manager to find to which COM port your Arduino is
connected to and correct the following line accordingly.
ArduinoSerial = serial.Serial('com18',9600)
#Create Serial port object called arduinoSerialData
time.sleep(2)
#wait for 2 seconds for the communication to get established
Inside the infinite while loop, we repeatedly listen to the COM port and compare the key words
with any pre-defied works and make key board presses accordingly.
while 1:
incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
print incoming
if 'Play/Pause' in incoming:
pyautogui.typewrite(['space'], 0.2)
if 'Rewind' in incoming:
pyautogui.hotkey('ctrl', 'left')
if 'Forward' in incoming:
pyautogui.hotkey('ctrl', 'right')
if 'Vup' in incoming:
pyautogui.hotkey('ctrl', 'down')
if 'Vdown' in incoming:
pyautogui.hotkey('ctrl', 'up')
