#!/usr/bin/python3.4

import wiringpi2 as wiringpi
from config import *
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
from datetime import timedelta
import datetime

c = Config()

scheduler = BackgroundScheduler()
scheduler.start()

wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)  # Set pin 0 to 1 ( OUTPUT )
wiringpi.digitalWrite(0, 0)  # deactivate pin


def timeLog():
    print("Time now: " + datetime.datetime.now().ctime())


scheduler.add_job(timeLog, trigger="interval", seconds=30)


def startWatering(duration):
    delta = datetime.datetime.now() + timedelta(seconds=duration)
    print("Start Watering")
    print("Stop Watering at: " + delta.ctime())
    wiringpi.digitalWrite(0, 1)  # Write 1 ( HIGH ) to pin 6
    # set timer to stop watering
    scheduler.add_job(stopWatering, trigger="date", run_date=delta)


def stopWatering():
    print("Stop Watering")
    wiringpi.digitalWrite(0, 0)


for w in c.water:
    scheduler.add_job(startWatering, trigger="cron", hour=w["hour"], minute=w["minute"], second=w["second"],
                      args=[w["duration"]])

while 1:
    sleep(1)
