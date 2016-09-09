# calvin 

A Raspberry Pi based vivarium thermostat/lighting controller

This file specifies the intended functionality of the application

I. Minimum Functionality Requirements

   1. Designed to run on Raspberry Pi/Raspbian
   2. Needs to run 24x7 (as a startup process?)
   3. Read raw digital input from sensors (temperature) and convert to human readable units (C/F) in real time 
   4. Thermostat- Switch multiple relays based on input from selected sensors and time of day (lower temps at night)
   5. Timer- Switch multiple relays based on date/time/scheduling (ie. lights on in the morning/off at night)
   6. Manual override for relay control  
   7. User accessible control panel/settings
   
 A. User Experience
 
    At initial launch, user will be presented a configuration flow in which they will be prompted to select a unit of temperature
    (C or F) and display the temperature readings according to the selection until it is changed again by the user via the settings.
    After this, the application will automatically detect any connected sensors and identify them to the user.  Once the sensors are 
    detected, the user will be prompted to label/name them.  After naming the sensor the user will will specify which sensor(s) will 
    be used for thermostat (if multiple, avg/RMS temp of selected sensors will be used).  Once the thermostat sensors have been 
    configured, the user will be prompted to select day and night time threshold temperatures, as well as times for light cycles.  The
    user can change these values any time via a control panel.  On each subsequent launch, the application will scan for any new 
    sensors that have been added since the last run, and prompt the user to label them if found.  Once configured and up and running, 
    application should be essentially "set it and forget it" with the exception of user intervention to make changes to settings. All
    configured settings will be retained if applications is stopped, and loaded automatically at next launch/reboot. 
   
   
 B. Current Components 

    - Raspberry Pi 3 B (1)
    - Raspbian (Jesse)
    - ds18b20 temperature sensor, waterproof (4)
            <http://www.ebay.com/itm/350842338983?_trksid=p2060353.m2749.l2649&ssPageName=STRK%3AMEBIDX%3AIT>

    - Four Channel Relay Module DC 5V With Optocoupler (1) 
           <http://www.ebay.com/itm/142054220831?_trksid=p2060353.m1438.l2649&ssPageName=STRK%3AMEBIDX%3AIT> 
     

 C. Resources and Inspiration
  
  - http://www.raspiviv.com/
  - https://pimylifeup.com/raspberry-pi-temperature-sensor/
  - http://bennet.org/blog/raspberry-pi-terrarium-controller/
  - https://github.com/skiwithpete/relaypi/tree/master/4port



II. Eventual Functionality
  
  1. Read raw digital hygrometer data and convert to human readable format (%RF)
  2. Admin/control console GUI 
    2a. web based admin console
  3. logging	
  4. Support for Pi Camera or webcam
  5. Arduino support
  6. Scalable/Modular - Ability to use as C&C platform for slave/satellite Pi/Arduino controlling other vivariums
  
  
  
