#!/usr/bin/python3.4

import wiringpi2 as wiringpi

print("Hallo")

wiringpi.wiringPiSetup()
wiringpi.pinMode(6,1) # Set pin 6 to 1 ( OUTPUT )
wiringpi.digitalWrite(6,1) # Write 1 ( HIGH ) to pin 6
