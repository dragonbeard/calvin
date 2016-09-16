#!/usr/bin/python3

import os
import glob
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM) # set board mode to broadcom
GPIO.setwarnings(False)

#GPIO.setup(6, GPIO.OUT) # set up pins for output mode
#GPIO.setup(6, GPIO.HIGH) # set pin states to high
#GPIO.setup(13, GPIO.OUT) # set up pin 13 for output
#GPIO.setup(13, GPIO.HIGH)
#GPIO.setup(19, GPIO.OUT) # set up pin 19 for output
#GPIO.setup(19, GPIO.HIGH)
#GPIO.setup(26, GPIO.OUT) #set up pin 26 for output 
#GPIO.setup(26, GPIO.HIGH)

pinList = [6, 13, 19, 26]
for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
device_file = (device_folder + '/w1_slave')


def read_temp_raw() :
    f = open(device_file[0], 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp() :
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':   #Checking for valid temperature reading.  If none found, wait and try again.
       time.sleep(0.2)
       lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:] #finds temp in raw input 
        temp_c = float(temp_string) / 1000.0  #convert raw input to *C 
        temp_f = temp_c * 9.0 / 5.0 + 32.0    #convertt to *F 
        return temp_f

try: 

   
  while True:
       
     print(read_temp())
     if read_temp() < 70.0 :     ###! Change this number to set thermostat  !###      
       GPIO.output(6, GPIO.LOW)  # turn on relay 1 when temp <  temp set above (* F)
     else:
       GPIO.output(6, GPIO.HIGH)  # turn off relay 1 when temp > temp set above (* F)  
       time.sleep(1)

except KeyboardInterrupt: 
    GPIO.cleanup()
    print("  ...Quitting")
