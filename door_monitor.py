#!/usr/bin/env python
# -*- coding: utf-8

import RPi.GPIO as GPIO
import time
import math


# # # # # # # # #
# Configuration #
# # # # # # # # #


# Pin number <-> hardware mappings
pin_button = 18
pin_led = 11

# Time between LED flashes (seconds)
led_flash_duration = 0.5
led_flash_separation = 2

# Alert Details
alert_duration = 30  # maximum number of minutes for which the flashes continue after door is closed.

# # # # # #
# Helpers #
# # # # # #


def door_is_closed():
    """Return (bool) whether door is currently closed."""
    return GPIO.input(pin_button) == 0


def led_on():
    """Turn the LED on."""
    print("Turning LED ON")
    GPIO.output(pin_led, GPIO.HIGH)


def led_off():
    """Turn the LED off."""
    print("Turning LED OFF")
    GPIO.output(pin_led, GPIO.LOW)


def flash_led():
    """Flash the LED once."""

    led_on()
    time.sleep(led_flash_duration)

    led_off()
    time.sleep(led_flash_separation)


def setup():

    # Set the pin numbering to "board" (not "BCM"/broadcom)
    GPIO.setmode(GPIO.BOARD)

    # Set up the button's pin as an input
    GPIO.setup(pin_button, GPIO.IN)
    # Set up the LED's pin as an output
    GPIO.setup(pin_led, GPIO.OUT)


# # # # #
# Logic #
# # # # #


def main():

    setup()

    if door_is_closed():
        print("Door is currently CLOSED")
    else:
        print("Door is currently OPEN")

    # Monitor switch for changes
    # We could use interrupts here, but polling is sufficient given the required time-frames.
    while True:

        time.sleep(0.5)  # free up CPU for other tasks!

        # Detect if door has been closed
        if door_is_closed():

            time_closed = time.time()
            print("Door closed at: %d" % time_closed)

            while True:

                seconds_closed = time.time() - time_closed
                #print("Door has been closed for %d second(s)." % seconds_closed)

                minutes_closed = int(math.floor(seconds_closed / 60))
                print("Door has been closed for %d minute(s)." % minutes_closed)

                num_flashes = minutes_closed + 1
                print("Flashing %d times." % num_flashes)

                for _ in range(0, num_flashes):
                    led_off()
                    time.sleep(0.2)
                    led_on()
                    time.sleep(0.2)
                    # allow for break if door opens while flashing
                    if not door_is_closed():
                        break

                if not door_is_closed():
                    print("Door is no longer closed")
                    led_off()
                    break

                # Stop flashing after 'alert_duration' minutes
                if minutes_closed > alert_duration:
                    print("Door has been closed for longer than %d minutes. Stop alert." % alert_duration)
                    led_off()
                    break

                time.sleep(2)

# # # # # #
# Wrapper #
# # # # # #

try:

    main()

except KeyboardInterrupt:
    # Code to run before the program exits after CTRL+C
    print("Stopping...")

finally:
    print("Cleaning up...")

    # this ensures a clean exit (resets pins to inputs)
    GPIO.cleanup()