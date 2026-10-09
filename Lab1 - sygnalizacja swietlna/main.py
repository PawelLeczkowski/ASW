import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

data = 20
clock = 21
buffer = 22
sector1 = 23
sector2 = 24
sector3 = 25
switch1 = 26
switch2 = 27

GPIO.setup(data, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
GPIO.setup(buffer, GPIO.OUT)
GPIO.setup(sector1, GPIO.OUT)
GPIO.setup(sector2, GPIO.OUT)
GPIO.setup(sector3, GPIO.OUT)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

bits = 0

def send_bits(bits_copy):
    GPIO.output(sector1, GPIO.HIGH)
    GPIO.output(sector2, GPIO.HIGH)
    GPIO.output(sector3, GPIO.HIGH)

    GPIO.output(sector3, GPIO.LOW)

    for i in range(47, -1, -1)
        GPIO.output(clock, GPIO.LOW)

        bit = (bits_copy >> i) & 1
        GPIO.output(clock, GPIO.HIGH)

    GPIO.output(buffer, GPIO.HIGH)

    GPIO.output(sector1, GPIO.HIGH)
    GPIO.output(sector2, GPIO.HIGH)
    GPIO.output(sector3, GPIO.HIGH)

licznik = 0
while True:
    if GPIO.input(switch1) == GPIO.LOW:
        print("switch1")

    if GPIO.input(switch2) == GPIO.LOW:
        print("switch2")

    send_bits(bits)
    bits = (1 << licznik)
    licznik += 1
    sleep(1)
    if licznik > 47:
        licznik = 0