#!/usr/bin/python3.4

import wiringpi2 as wiringpi
from config import *
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
from datetime import timedelta
import datetime
import logging

c = Config()
waterpin = c.hardware["waterpin"] #["hardware"]["waterpin"]
logging.basicConfig(filename=c.software["logfile"], level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%d.%m.%Y %I:%M:%S")

scheduler = BackgroundScheduler()
scheduler.start()

wiringpi.wiringPiSetup()
wiringpi.pinMode(waterpin, 1)  # Set waterpin to 1 ( OUTPUT )
wiringpi.digitalWrite(waterpin, 0)  # deactivate pin


def startWatering(duration):
    delta = datetime.datetime.now() + timedelta(seconds=duration)
    logging.debug("Start Watering")
    logging.debug("Start Stop Watering at: " + delta.ctime())
    wiringpi.digitalWrite(waterpin, 1)  # Write 1 ( HIGH ) to pin 6
    # set timer to stop watering
    scheduler.add_job(stopWatering, trigger="date", run_date=delta)


def stopWatering():
    logging.debug("Stop Watering")
    wiringpi.digitalWrite(waterpin, 0)


for w in c.water:
	logging.debug("Adding Water job for setpoint: " + str(w["hour"]) + ":" + str(w["minute"]) + ":" + str(w["second"]) + " for duration: " + str(w["duration"]))
	scheduler.add_job(startWatering, trigger="cron", hour=w["hour"], minute=w["minute"], second=w["second"],args=[w["duration"]])

while 1:
    sleep(1)
