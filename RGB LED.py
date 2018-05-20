from machine import Pin
from machine import PWM
from time import sleep


red = Pin(0, Pin.OUT, Pin.PULL_UP)
green = Pin(2, Pin.OUT, Pin.PULL_UP)
blue = Pin(4, Pin.OUT, Pin.PULL_UP)
button = Pin(5, Pin.IN)


def lights_on(R=1, G=1, B=0):
  if R == 1:
    red.on()
  else:
    red.off()
  if G == 1:
    green.on()
  else:
    green.off()
  if B == 1:
    blue.on()
  else:
    blue.off()


def lights_off():
  red.off()
  green.off()
  blue.off()


def Lights_on_button():
  on_of = 0
  while True:
    if button.value() == 0:
        on_of += 1
    if on_of % 2 == 0:
      lights_on()
    else:
      lights_off()
    print(on_of)
    sleep(1)


def osciloscope(P1=.2, P2=.5):
  while True:
    sleep(P1)
    lights_on()
    sleep(P2)
    lights_off()


def PWM_light(R, G, B, F1, F2 , F3):
  R = int((R/255)*1023)
  G = int((G/255)*1023)
  B = int((B/255)*1023)
  PWM(red, freq=F1, duty=R)
  PWM(green, freq=F2, duty=G)
  PWM(blue, freq=F3, duty=B)


def PWM_light_button(R, G, B, F1, F2 , F3):
  R = int((R/255)*1023)
  G = int((G/255)*1023)
  B = int((B/255)*1023)
  while True:
    button_value = button.value()
    if button_value == 1:
      PWM(red, freq=F1, duty=R)
      PWM(green, freq=F2, duty=G)
      PWM(blue, freq=F3, duty=B)
    else:
      PWM(red, freq=0, duty=0)
      PWM(green, freq=0, duty=0)
      PWM(blue, freq=0, duty=0)
    sleep(.01)


#PWM_light(0,0,250,0,0,400)
#lights_on(1, 1, 0)
#Lights_on_button()
#osciloscope(.1, .2)
