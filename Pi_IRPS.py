import RPi.GPIO as GPIO
import time

Pin = 22  # GPIO Pin 22
data = []

GPIO.setmode(GPIO.BCM)

# Setup light sensor pin status
GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, GPIO.LOW)
time.sleep(0.5)
GPIO.output(Pin, GPIO.HIGH)
GPIO.setup(Pin, GPIO.IN)

try:
    print("IRPS Online")
    i = 0
    while True:
        while GPIO.input(channel) == GPIO.LOW:
            continue
        while GPIO.input(channel) == GPIO.HIGH:
            continue
        while i < 40:
            k = 0
            while GPIO.input(channel) == GPIO.LOW:
                continue
            while GPIO.input(channel) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
            if k < 8:
                data.append(0)
            else:
                data.append(1)
            i += 1
        bit = data[0:8]
        point_bit = data[8:16]
        num = 0
        num_point = 0
        for i in range(8):
            num += bit[i] * 2 ** (7 - i)
            num_point += point_bit[i] * 2 ** (7 - i)
        print(num, ".", num_point)
        time.sleep(2)

except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    print("IRPS Outline")
    pass