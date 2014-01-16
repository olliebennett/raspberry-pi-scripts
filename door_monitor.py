#!/usr/bin/env python
# -*- coding: utf-8

import RPi.GPIO as GPIO
import time

# # # # # # # # #
# Configuration #
# # # # # # # # #

# Pin number <-> hardware mappings
pin_button = 18
pin_led = 11

# Time between LED flashes (seconds)
led_flash_duration = 0.5
led_flash_separation = 2

# Monitor start



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

  # Monitor switch for changes
  while True:

    time.sleep(0.1) # free up CPU for other tasks!

    if door_is_closed():
      flash_led()

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

