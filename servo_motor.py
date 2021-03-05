import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Servo:
  def __init__(self, top_servo, bottom_servo):
    self.top_servo = top_servo #4
    self.bottom_servo = bottom_servo #3
    GPIO.setup(self.top_servo, GPIO.OUT)
    self.top_pwm = GPIO.PWM(self.top_servo, 50) # 50 is frequenc
    GPIO.setup(self.bottom_servo, GPIO.OUT)
    self.bottom_pwm = GPIO.PWM(self.bottom_servo, 50)
    self.top_pwm.start(0)
    self.bottom_pwm.start(0)
    
  def position1(self):
    self.bottom_pwm.ChangeDutyCycle(10)
    sleep(1)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
 
  def position2(self):
    self.bottom_pwm.ChangeDutyCycle(8)
    sleep(1)
    self.top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
  def position3(self):
    self.bottom_pwm.ChangeDutyCycle(6)
    sleep(1)
    self.top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
  def position4(self):
    self.bottom_pwm.ChangeDutyCycle(4)
    sleep(1)
    self.top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
  def position5(self):
    self.bottom_pwm.ChangeDutyCycle(2)
    sleep(1)
    self.top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    self.top_pwm.ChangeDutyCycle(15)
    sleep(0.4) 
