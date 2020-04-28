Raspberry Pi Scripts
====================

Scripts created by [Ollie Bennett](https://www.olliebennett.co.uk/) to run on [@Ollie_RPi](https://twitter.com/Ollie_RPi).

## Initial Pi Setup

- Boot the Pi headless by adding a `ssh` file in the SD card's boot partition.

- SSH in using `ssh pi@raspberrypi`; password is `raspberry`. Change that with `passwd`.

- Update everything with `sudo apt-get update && sudo apt-get full-upgrade`

- Install `git` with `sudo apt-get install git`.

- Enable camera via `sudo raspi-config` -> `Interfacing Options` -> `Camera`.

- Clone this repo with `git clone --recurse-submodules https://github.com/olliebennett/raspberry-pi-scripts.git`

## Web Server

- Install Flask;

  ```bash
  sudo apt-get install python3-flask
  ```

- Start the server with

  ```bash
  sudo python3 flask_server.py
  ```

- Visit the page via [http://raspberrypi/](http://raspberrypi/)!

## Camera Streaming



  ```bash
  sudo apt-get install python3-picamera
  sudo apt-get install python3-opencv
  ```

- Run the server again as outlined above.
