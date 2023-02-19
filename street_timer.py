import time

class Street_Timer:
  
  def __init__(self, people, wc, cane):
    self.people = people
    self.wc = wc
    self.cane = cane


  def lights_control(self, delay):
    red = delay
    yellow = delay
    green = delay
    return
  
  def get_delay(self):
    return 10.0 + self.people*0.2 + self.wc*3.0 + self.cane*1.5

def main():
  delay = 10.0
  Street_Timer.lights_control(delay)

if __name__ == '__main__' :
  main()	