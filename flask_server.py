#!/usr/bin/env python

from flask import Flask, render_template, send_from_directory, flash
import os
import platform
from time import gmtime, strftime
from datetime import timedelta
import olliebennett.logger as Log

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("home.html")


@app.route("/shutdown")
def route_shut_down():
    Log.info(Log.SERVER, "Request for shutdown received!")

    os.system("sudo shutdown -h now")

    flash("The shutdown procedure has commenced. All Raspberry Pi functions will now stop.", "info")
    return render_template("layout.html", title="Shutdown")


@app.route('/torrents')
def route_torrents():
    return render_template("torrents.html", title="Torrents")


@app.route('/shared-files')
def route_shared_files():
    return render_template("shared-files.html", title="Shared Files")


@app.route('/stats')
def route_stats():

    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds=uptime_seconds))

            print(uptime_string)

    except FileNotFoundError:  # is this running outside the RPi?
        uptime_string = "[ value could not be determined ]"

    time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if "getloadavg" in dir(os):
        load_average = os.getloadavg()
    else:
        load_average = "[ value could not be determined ]"

    server_platform_full = platform.platform()
    # detect
    if "Windows" in server_platform_full:
        server_platform = "windows"
    elif "Linux" in server_platform_full:
        server_platform = "linux"
    else:
        server_platform = "question"  # use "question" because it matches a font awesome icon name

    python_version = "v " + platform.python_version() + " (" + platform.python_implementation() + ")"

    # Collect statistics about this Raspberry Pi
    stats = dict(
        uptime=uptime_string,
        time_now=time_now,
        load_average=load_average,
        server_platform=server_platform,
        server_platform_full=server_platform_full,
        python_version=python_version
    )

    return render_template("stats.html", title="Stats", stats=stats)


@app.route('/favicon.ico')
def route_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

app.secret_key = '2\x1f\xfb\xf5)7\x13=\r\x85\xdd;\x1fpBx\xce`\xd0\xa7\x86)?\xb4'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)



