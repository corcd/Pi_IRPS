import RPi.GPIO as GPIO
import time

Pin = 22  # GPIO Pin 22
data = []

alpha = 0.75

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
    value = 0
    oldValue = 0
    while True:
        while GPIO.input(Pin) == GPIO.LOW:
            continue
        while GPIO.input(Pin) == GPIO.HIGH:
            continue
        while i < 8:
            k = 0
            while GPIO.input(Pin) == GPIO.LOW:
                continue
            while GPIO.input(Pin) == GPIO.HIGH:
                k += 1
                if k > 1000:
                    break
            if k < 8:
                data.append(0)
                print("0")
            else:
                data.append(1)
                print("1")
            i += 1
        bit = data[0:8]
        num = 0
        for i in range(8):
            num += bit[i] * 2 ** (7 - i)

        rawValue = num
        value = alpha * oldValue + (1 - alpha) * rawValue;
        print(rawValue,value)
        oldValue = value
        time.sleep(2)

except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    print("IRPS Outline")
    pass