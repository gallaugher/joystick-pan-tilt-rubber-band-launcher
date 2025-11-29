# Use this to move the servo to the 90° position before you add the servo horn in the position 
# so that the arm points straight up.
import time, board,  pwmio
from adafruit_motor import servo 

pwm_y = pwmio.PWMOut(board.GP12, frequency=50)  # Y axis (tilt)
y_servo = servo.Servo(pwm_y, min_pulse=650, max_pulse=2350)

y_servo.angle = 0
print("servo at angle 0°")
time.sleep(3)

# Set initial angles at 90°
y_servo.angle = 90
print("servo at angle 0°")
time.sleep(3) # necessary before the program ends to give servo enough time after receiving the angle.
# You could also put in a while True: just don't stop right after setting the angle
