import RPi.GPIO as GPIO
import noDelayIO as mio
import time
millis = int(round(time.time() * 1000))
#startTime = millis
LedPin = 11  # LED No. 1
Led2Pin = 7  # LED No. 2
Led3Pin = 19 # LED No. 3

sw1Pin = 40  # Switch No. 1

blinkPeriod = 5000
swPeriod = 20
dbTime = 2000

# Instantiate three objects of the class "Lampy"
# In future, investigate where else these might be created
Lamp1 = mio.Lampy(LedPin,blinkPeriod)
Lamp2 = mio.Lampy(Led2Pin,int(blinkPeriod*4/3))
Lamp3 = mio.Lampy(Led3Pin,int(blinkPeriod*4/7))

Switch1 = mio.Switchy(sw1Pin,swPeriod,dbTime)

def setup():
    #*** Uncomment out these lines for use on RPi ***
    # Use Physical Pin Number rather than silkscreen
    GPIO.setmode(GPIO.BOARD)
    print("in setup")
    GPIO.setup(LedPin, GPIO.OUT)   
    GPIO.output(LedPin, GPIO.HIGH)
    
    GPIO.setup(Led2Pin, GPIO.OUT)   
    GPIO.output(Led2Pin, GPIO.HIGH)

    GPIO.setup(sw1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
    while True:
        millis = int(round(time.time() * 1000))
        Lamp1.time = millis
        Lamp2.time = millis
        #Lamp3.time = millis
        Lamp1.LampCheck()
        Lamp2.LampCheck()
        #Lamp3.LampCheck()

        #until we hook it up to real IO, use the pretend
        # lamp1 state to simulate a switch input.
        #Switch1.rawState = Lamp1.lampState
        Switch1.time = millis
        Switch1.debounce()

def destroy():
    GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        destroy()
