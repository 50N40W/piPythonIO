#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:16:55 2019

@author: hb
"""
import time
#******************************************
# The Class "Lampy" is defined here
class Lampy:
    """ the lamp processing things here """
    def __init__(self, pin, period):
        self.gpio_pin = pin
        self.period = period
        self.lamp_state = "low"
        self.previous = 0
        self.time = 0

    def lamp_check(self):
        """
        within Lampy, create a method to check lamp timer
         and if expired, to swap the LED between off and on
         """
        return_time = self.time
        if self.time - self.previous > self.period:
            return_time = int(round(time.time() * 1000))
            self.previous = self.time
            if self.lamp_state == "low":
                self.lamp_state = "high"
            else:
                self.lamp_state = "low"
        return return_time
    def lamp_override(self, override_value):
        """
        make a lamp override possible
        """
        self.lamp_state = override_value
            #print(str(self.gpioPin) + ' ' + str(self.lampState))
# This ends the definition of "Lampy"
#******************************************

#******************************************
# The class "Switchy" is like Lampy, but for a switch input
class Switchy:
    """
    items for switch processing
    """
    def __init__(self, pin, period, saturation):
        self.sw_pin = pin
        self.db_period = period
        self.db_time = saturation
        self.time = 0
        self.db_ctr = 0
        self.prev_db_ctr = 0
        self.switch_state = False

    # the debounce method exists to debounce a switch
    def debounce(self):
        """ debounce switch input"""
        prev_switch = self.switch_state
        return_time = self.time
        if self.time > self.db_period:
            return_time = int(round(time.time() * 1000))
            self.db_ctr = min(self.db_time, self.db_ctr+self.db_period)
            if self.db_ctr >= self.db_time:
                self.switch_state = True
            else:
                self.db_ctr = max(0, self.db_ctr-self.db_period)
                if self.db_ctr <= 0:
                    self.switch_state = False
            if self.db_ctr != self.prev_db_ctr:
                self.prev_db_ctr = self.db_ctr
            if prev_switch != self.switch_state:
                print(self.switch_state)
        return return_time

    def get_switch_value(self):
        """ get the switch state
        """
        return self.switch_state
