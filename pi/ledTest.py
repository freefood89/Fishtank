
from RPIO import PWM
import time

servo = PWM.Servo()
LED = 17

time.sleep(1)
servo.set_servo(LED,1000)
time.sleep(1)
servo.set_servo(LED,0)
time.sleep(1)
servo.set_servo(LED,1000)
time.sleep(1)
servo.stop_servo(LED)

