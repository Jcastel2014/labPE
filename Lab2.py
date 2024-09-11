//1.
    import RPi.GPIO as GPIO
    import time

    # Set up the GPIO pin
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(17, GPIO.OUT)  # GPIO 17 as output

    try:
        while True:
            GPIO.output(17, GPIO.HIGH)  # Turn LED on
            time.sleep(1)               # Wait 1 second
            GPIO.output(17, GPIO.LOW)   # Turn LED off
            time.sleep(1)               # Wait 1 second
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # Clean up resources
        
        
//2.
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    red, yellow, green = 17, 27, 22

    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(yellow, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)

    try:
        while True:
            # Red light
            GPIO.output(red, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(red, GPIO.LOW)

            # Green light
            GPIO.output(green, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(green, GPIO.LOW)

            # Yellow light
            GPIO.output(yellow, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(yellow, GPIO.LOW)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        
//3.

    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    leds = [17, 27, 22]

    for led in leds:
        GPIO.setup(led, GPIO.OUT)

    try:
        while True:
            # Light up each LED in sequence
            for led in leds:
                GPIO.output(led, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(led, GPIO.LOW)

            # Light up each LED in reverse sequence
            for led in reversed(leds):
                GPIO.output(led, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(led, GPIO.LOW)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
