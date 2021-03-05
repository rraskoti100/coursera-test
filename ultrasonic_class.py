import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Ultrasonic:
  def __init__(self, TRIG, ECHO):
    self.TRIG = TRIG #3
    self.ECHO = ECHO #4
    self.maxtime = 0.04
    GPIO.setup(self.TRIG, GPIO.OUT)
    GPIO.setup(self.ECHO, GPIO.IN)


  def distance():
      GPIO.output(self.TRIG, False)
      time.sleep(0.01)
      GPIO.output(self.TRIG, True)
      time.sleep(0.00001)
      GPIO.output(self.TRIG, False)

      start_time = time.time()
      timeout = start_time + self.maxtime
      while GPIO.input(self.ECHO) == 0 and start_time < timeout:
          start_time = time.time()

      end_time = time.time()
      timeout = end_time + maxtime
      while GPIO.input(self.ECHO) == 1 and end_time < timeout:
          end_time = time.time()

      t = end_time - start_time
      dist = (t*34300)//2
      return dist
