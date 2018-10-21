import RPi.GPIO as GPIO
import time
import noDelayIO as mio

millis = int(round(time.time() * 1000))
#startTime = millis
LedPin = 11  # LED No. 1
Led2Pin = 7  # LED No. 2
Led3Pin = 19 # LED No. 3
blinkPeriod = 500

sw1Pin = 40  # Switch No. 1
swPeriod = 20
dbTime = 900

# Instantiate three objects of the class "Lampy"
# In future, investigate where else these might be created
Lamp1 = mio.Lampy(LedPin,blinkPeriod)
Lamp2 = mio.Lampy(Led2Pin,int(blinkPeriod*4/3))
Lamp3 = mio.Lampy(Led3Pin,int(blinkPeriod*4/7))

Switch1 = mio.Switchy(sw1Pin,swPeriod,dbTime)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Lamp1.gpioPin, GPIO.OUT)   
    GPIO.output(Lamp1.gpioPin, GPIO.HIGH)
    GPIO.setup(Lamp2.gpioPin, GPIO.OUT)   
    GPIO.output(Lamp2.gpioPin, GPIO.HIGH)
    GPIO.setup(Lamp3.gpioPin, GPIO.OUT)   
    GPIO.output(Lamp3.gpioPin, GPIO.HIGH)
    
    GPIO.setup(Switch1.swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def loop():
    while True:
        # we could invoke time in each objects
        # method.   But that means 3 sys calls
        # per loop. This way takes only 1 call.
        millis = int(round(time.time() * 1000))
        Lamp1.time = millis
        Lamp2.time = millis
        Lamp3.time = millis
        Switch1.time = millis

        Switch1.rawState = GPIO.input(Switch1.swPin)
        Switch1.debounce()
        #if sw1 is "hot" change the lamp1 period
        if (Switch1.switchState == True):
            Lamp1.period = 10
            Lamp2.period = 1000
        else:
            Lamp1.period = blinkPeriod
            Lamp2.period = int(blinkPeriod*4/3)
        
        Lamp1.LampCheck()
        Lamp2.LampCheck()
        Lamp3.LampCheck()          
        if (Lamp1.time != Lamp1.previous):
            if (Lamp1.lampState == "high"):
                GPIO.output(Lamp1.gpioPin,GPIO.HIGH)
            else:
                GPIO.output(Lamp1.gpioPin,GPIO.LOW)
        if (Lamp2.time != Lamp2.previous):
            if (Lamp2.lampState == "high"):
                GPIO.output(Lamp2.gpioPin,GPIO.HIGH)
            else:
                GPIO.output(Lamp2.gpioPin,GPIO.LOW)
 
def destroy():
    GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.output(Led2Pin, GPIO.LOW)     # led off
    GPIO.output(Led3Pin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        destroy()
