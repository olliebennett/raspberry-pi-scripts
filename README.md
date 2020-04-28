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

- Change into the directory; `cd raspberry-pi-scripts`

## Web Server

- Install Flask;

  ```bash
  sudo apt-get install python3-flask
  ```

- Start the server with

  ```bash
  sudo ./flask_server.py
  ```

- Visit the page via [http://raspberrypi/](http://raspberrypi/)!

## Camera Streaming

- Install the `picamera` dependency.

  ```bash
  sudo apt-get install python3-picamera
  ```

- Run the server again as outlined above.
