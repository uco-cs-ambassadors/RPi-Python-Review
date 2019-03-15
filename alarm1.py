## Must create a folder on desktop named "Pics"
#import necessary libraries
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from gpiozero import LED, Buzzer, MotionSensor
from picamera import PiCamera
from datetime import datetime   # To get current date and time
from time import sleep          # To easily use sleep function

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

#RPi pin configuration
buzzer = Buzzer(27)
led = LED(5)
pir = MotionSensor(17)
camera = PiCamera()

#control variables
motion_sensor_on = False
alarmTriggered = False
lcd.clear()
lcd.color = [50, 0, 50]
led.off()


def alarm_on():
    # To change the initialized variable above, must redefine it here as 'global'
    global motion_sensor_on
    motion_sensor_on = True
    lcd.clear()
    lcd.color = [0, 50, 0]
    lcd.message = 'Alarm is on \nin 5 sec'
    sleep(1)
    # Give user time to leave the home
    for i in range (5):
        lcd.clear()
        lcd.message = str(i + 1)
        sleep(1)
    lcd.clear()
    lcd.message = 'Alarm is on'
    
def alarm_off():
    global motion_sensor_on
    motion_sensor_on = False
    global alarmTriggered
    alarmTriggered = False
    led.off()
    buzzer.off()
    lcd.clear()
    lcd.color = [0, 50, 50]
    lcd.message = 'Alarm is off'
    if camera.recording:
        camera.stop_recording()

def take_picture():
    for i in range(3):
        camera.capture('/home/pi/Desktop/Pics/image%s.jpg' % str(datetime.now()))
        sleep(0.5)

def shoot_video():
    if camera.recording == False:
        camera.start_recording('/home/pi/Desktop/Pics/video%s.mjpeg' % str(datetime.now()))

def sound_alarm():
    global alarmTriggered
    alarmTriggered = True
    lcd.clear()
    lcd.color = [50, 0, 0]
    lcd.message = 'Motion detected!'
    led.blink()
    buzzer.blink()
    take_picture()
    shoot_video()
            
while True:
    # Wait for a button press
    if lcd.select_button:
        if motion_sensor_on:
            alarm_off()
        else:
            alarm_on()
    # Define actions that occur if the alarm is on
    if motion_sensor_on:
        # If alarm has not yet been triggered, check the motion sensor
        if (alarmTriggered == False):
            if pir.motion_detected:
                # Note that this function sets alarmTriggered to 'true'
                sound_alarm()
        # If alarm was triggered, it will continue to sound until user
        # turns it off
        else:
            if lcd.select_button:
                # Note that this functon sets alarmTriggered to 'false'
                alarm_off()
