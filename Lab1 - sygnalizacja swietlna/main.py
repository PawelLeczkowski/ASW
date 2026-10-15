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

GPIO.setup(data, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(clock, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buffer, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(sector1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(sector2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(sector3, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_bits(bits_copy):
    GPIO.output(sector1, GPIO.HIGH)
    GPIO.output(sector2, GPIO.HIGH)
    GPIO.output(sector3, GPIO.HIGH)

    for i in range(47, -1, -1):
        GPIO.output(clock, GPIO.LOW)

        bit = (bits_copy >> i) & 1
        GPIO.output(data, bit)

        GPIO.output(clock, GPIO.HIGH)

    GPIO.output(clock, GPIO.LOW)
    GPIO.output(buffer, GPIO.LOW)
    GPIO.output(buffer, GPIO.HIGH)

    GPIO.output(sector1, GPIO.LOW)
    GPIO.output(sector2, GPIO.LOW)
    GPIO.output(sector3, GPIO.LOW)

def make_bits(*numbers):
    bits = 0
    for n in numbers:
        bits |= 1 << n
    return bits

# Sygnalizacja dla pieszych
def set_pedestrians():
    # Zolte dla wszystkich
    send_bits(make_bits(1, 9, 17, 29, 33, 46))
    sleep(3)

    # Czerwone dla wszystkich
    send_bits(make_bits(0, 8, 16, 30, 32, 47))
    sleep(1)

    # Zielone dla pieszych
    send_bits(make_bits(
        5, 6, 13, 14, 21, 23,
        25, 26, 37, 39, 42, 43
    ))
    sleep(10)

    # Czerwone dla pieszych
    send_bits(make_bits(
        4, 7, 12, 15, 20, 22,
        24, 27, 36, 38, 41, 44
    ))
    sleep(1)

    # Zolte i czerwone dla drogi glownej
    send_bits(make_bits(0, 1, 8, 9))
    sleep(1)

    # Zielone dla drogi glownej
    send_bits(make_bits(2, 10))
    sleep(1)

    # Zielona strzalka dla drogi malej
    send_bits(make_bits(19, 35))


# Samochody na drodze glownej
def set_cars_main():
    # Droga glowna: zielone
    # Droga mala: czerwone
    send_bits(make_bits(2, 10, 16, 32))

    while True:
        # Przycisk 1 - zmiana kierunku ruchu
        if GPIO.input(switch1) == GPIO.LOW:
            sleep(0.05)
            if GPIO.input(switch1) == GPIO.LOW:
                set_cars_small()
                return

        # Przycisk 2 - przejscie dla pieszych
        if GPIO.input(switch2) == GPIO.LOW:
            sleep(0.05)
            if GPIO.input(switch2) == GPIO.LOW:
                set_pedestrians()
                return

        sleep(0.05)


# Samochody na drodze podporzadkowanej
def set_cars_small():
    # Zolte dla drogi glownej
    send_bits(make_bits(1, 9, 16, 32))
    sleep(3)

    # Czerwone dla glownej, czerwone dla malej
    send_bits(make_bits(0, 8, 16, 32))
    sleep(1)

    # Zielone dla drogi malej
    send_bits(make_bits(2, 10, 16, 32))
    sleep(1)

    # Zielone dla glownej, czerwone dla malej
    send_bits(make_bits(2, 10, 16, 32))

try:
    while True:
        set_cars_main()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()