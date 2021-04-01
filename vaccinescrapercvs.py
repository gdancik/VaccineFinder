# Vinny's Vaccine Finder

# Scrapes data from CVS in CT

import time
import random
from os import path

import vaccine
import credentials

RUNNING_TIME = 2   # running time in minutes
MIN_SLEEP = 25      # minimum sleep time between searches, in seconds
MAX_SLEEP = 65      # maximum sleep time between searches, in seconds

start = time.time()

# run for RUNNING_TIME minutes
while time.time() - start < RUNNING_TIME*60 :
    
    # check availability and send message
    vax = vaccine.check_cvs()
    vaccine.send_msg(credentials.sender, credentials.to, vax.msg, credentials.password)

    # sleep
    r = random.randint(MIN_SLEEP, MAX_SLEEP)
    time.sleep(r)

