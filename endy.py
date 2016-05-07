from pync import Notifier
import json
import time
import random

FILE_NAME = 'data/UI2.json'

with open(FILE_NAME) as data_file:    
    data = json.load(data_file)
    count = len(data["words"])

    while True:
    	ind = int( random.random()*count )
    	word = data["words"][ind]
    	Notifier.notify(word["ua"].encode('utf-8'), title=word["en"])
    	time.sleep(25)


