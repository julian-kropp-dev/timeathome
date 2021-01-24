#Time@HomeProject by Julian K., 2020
import time
import csv
import datetime
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


def LED():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
while True:
    try:
        print("Bitte RFID Chip/Karte vorlegen!")
        id = reader.read()
        ts = time.time()
        text = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        with open("Datenbank.txt", "a", newline="") as f:
            twriter = csv.writer(f)
            twriter.writerow([id[0], text, round(ts,2)])
        print("Uhrzeit aktualisiert: " + text)
        LED()
        time.sleep(5)
    finally:
        GPIO.cleanup()
