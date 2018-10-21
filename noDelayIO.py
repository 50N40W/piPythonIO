import RPi.GPIO as GPIO

#******************************************                        
# The Class "Lampy" is defined here
class Lampy:
    def __init__(self,pin,period):
        self.gpioPin = pin
        self.period = period
        self.lampState = "low"
        self.previous = 0
        self.override = False
        self.overrideValue = "low"
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.gpioPin, GPIO.OUT)   
        GPIO.output(self.gpioPin, GPIO.HIGH)
    
    #within Lampy, create a method to check lamp timer
    # and if expired, to swap the LED between off and on
    def LampCheck(self):
        if self.override == True:
            if self.overrideValue == "high":
                GPIO.output(self.gpioPin, GPIO.HIGH)
            else:
                GPIO.output(self.gpioPin, GPIO.LOW)
        else:
            if self.time - self.previous > self.period:
                self.previous = self.time
                if self.lampState == "low":
                    self.lampState = "high"
                    GPIO.output(self.gpioPin, GPIO.HIGH) 
                else:
                    self.lampState = "low"    
                    GPIO.output(self.gpioPin, GPIO.LOW)
            #print(str(self.gpioPin) + ' ' + str(self.lampState))
# This ends the definition of "Lampy"
#******************************************

#******************************************
# The class "Switchy" is like Lampy, but for a switch input
class Switchy:
    def __init__(self,pin,period,saturation):
        self.swPin = pin
        self.dbPeriod = period
        self.dbTime = saturation
        self.time = 0
        self.previous = 0
        self.dbCtr = 0
        self.prevdbCtr = 0
        self.switchState = False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # the debounce method exists to debounce a switch
    def debounce(self):
        self.rawState = GPIO.input(self.swPin)
        #self.rawState = GPIO.input(18)
        if self.time - self.previous > self.dbPeriod:
            self.previous = self.time
            if self.rawState == True:
                print("      ++++++")
            else:
                print("______")
            if self.rawState == False:
                self.dbCtr = min(self.dbTime, self.dbCtr+self.dbPeriod)
                if self.dbCtr >= self.dbTime:
                    self.switchState = True
            else:
                self.dbCtr = max(0, self.dbCtr-self.dbPeriod)
                if self.dbCtr <= 0:
                    self.switchState = False
            if self.dbCtr != self.prevdbCtr:
                print(self.dbCtr)
                self.prevdbCtr = self.dbCtr
