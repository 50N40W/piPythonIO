 -*- coding: utf-8 -*-
"""
#import RPi.GPIO as GPIO
import time
import no_delay_io as mio


#startTime = millis
LEDPIN = 11  # LED No. 1
LED2PIN = 7  # LED No. 2
LED3PIN = 19 # LED No. 3
BLINKPERIOD = 500

SW1PIN = 40  # Switch No. 1
SWWPERIOD = 20
DBTIME = 900

# Instantiate three objects of the class "Lampy"
# In future, investigate where else these might be created


#def setup():

#    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(Lamp1.gpioPin, GPIO.OUT)
#    GPIO.output(Lamp1.gpioPin, GPIO.HIGH)
#    GPIO.setup(Lamp2.gpioPin, GPIO.OUT)
#    GPIO.output(Lamp2.gpioPin, GPIO.HIGH)
#    GPIO.setup(Lamp3.gpioPin, GPIO.OUT)
#    GPIO.output(Lamp3.gpioPin, GPIO.HIGH)

#    GPIO.setup(Switch1.swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def loop():
    """
    takes care of the near real time task of reading switch
    and checking time
    """
    lamp1 = mio.Lampy(LEDPIN, LEDPIN)
    lamp2 = mio.Lampy(LED2PIN, int(BLINKPERIOD*4/3))
    #Lamp3 = mio.Lampy(LED3PIN, int(BLINKPERIOD*4/7))
    switch1 = mio.Switchy(SW1PIN, SWWPERIOD, DBTIME)
    millis = int(round(time.time() * 1000))
    while True:
        # we could invoke time in each objects
        # method.   But that means 3 sys calls
        # per loop. This way takes only 1 call.
        millis = int(round(time.time() * 1000))
        lamp1.time = millis
        lamp2.time = millis
        #Lamp3.time = millis
        switch1.time = millis

        #Switch1.rawState = GPIO.input(Switch1.swPin)
        switch1.debounce()
        #if sw1 is "hot" change the lamp1 period
        if switch1.switch_state:
            lamp1.period = 10
            lamp2.period = 1000
        else:
            lamp1.period = BLINKPERIOD
            lamp2.period = int(BLINKPERIOD*4/3)

        lamp1_previous = lamp1.lamp_check()
        lamp2_previous = lamp2.lamp_check()
        #Lamp3_previous = Lamp3.lamp_check()
        if lamp1.time != lamp1_previous:
            if lamp1.lamp_state == "high":
                print("lamp1 h")
                #GPIO.output(Lamp1.gpioPin, GPIO.HIGH)
            else:
                print("lamp1 L")
                #GPIO.output(Lamp1.gpioPin, GPIO.LOW)
        if lamp2.time != lamp2_previous:
            if lamp2.lamp_state == "high":
                print("lamp2 h")
                #GPIO.output(Lamp2.gpioPin, GPIO.HIGH)
            else:
                print("lamp2 L")
                #GPIO.output(Lamp2.gpioPin, GPIO.LOW)

def destroy():
    """
    clean things up at the end
    """
    print("good bye")
#    GPIO.output(LEDPIN, GPIO.LOW)     # led off
#    GPIO.output(LED2PIN, GPIO.LOW)     # led off
#    GPIO.output(LED3PIN, GPIO.LOW)     # led off
#    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    try:
        #setup()
        print("begin")
        loop()
        print("end")
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        print("the end")
        #destroy()
