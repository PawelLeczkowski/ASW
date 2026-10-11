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
        GPIO.output(data, bit)

        GPIO.output(clock, GPIO.HIGH)

    GPIO.output(buffer, GPIO.HIGH)

    GPIO.output(sector1, GPIO.HIGH)
    GPIO.output(sector2, GPIO.HIGH)
    GPIO.output(sector3, GPIO.HIGH)

def make_bits(*numbers):
    bits = 0
    for n in numbers:
        bits |= 1 << n
    return bits

def set_pedestrians():
    # zolte dla wszystkich
    send_bits(make_bits(1, 9, 17, 29, 33, 46))
    sleep(3)
    # czerwone dla wszystkich
    send_bits(make_bits(0, 8, 16, 30, 32, 47))
    sleep(1)
    # zielone dla pieszych
    send_bits(make_bits(5, 6, 13, 14, 21, 23, 25, 26, 37, 39, 42, 43))
    sleep(10)# piesi se ida
    # czerwone dla pieszych
    send_bits(make_bits(4, 7, 12, 15, 20, 22, 24, 27, 36, 38, 41, 44))
    sleep(1)
    # zolte i czerwone dla glownej drogi
    send_bits(make_bits(0, 1, 8, 9))
    sleep(1)
    # zielone dla glownej drogi
    send_bits(make_bits(2, 10))
    sleep(1)
    # zielona strzalka dla malej drogi
    send_bits(make_bits(19, 35))

def set_cars_main():
    # zolte dla malej drogi
    # czerwone dla malej drogi
    # zolte i czerwone dla malej drogi
    # zielone dla malej drogi
    pass

def set_cars_small():
    # zolte dla glownej drogi
    # czerwone dla glownej drogi
    # zolte i czerwone dla glownej drogi
    # zielone dla glownej drogi
    pass

#licznik = 0

set_cars_main()

while True:
    if GPIO.input(switch1) == GPIO.LOW:
        print("cars change")

    if GPIO.input(switch2) == GPIO.LOW:
        print("pedestrians")
        set_pedestrians()

'''
    send_bits(bits)
    bits = (1 << licznik)
    licznik += 1
    sleep(1)
    if licznik > 47:
        licznik = 0
'''
