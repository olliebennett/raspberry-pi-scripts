#!/usr/bin/env python

from flask import Flask, render_template, send_from_directory, flash
import os
import olliebennett.logger as Log

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("layout.html")


@app.route("/shutdown")
def shut_down():
    Log.info(Log.SERVER, "Request for shutdown received!")

    os.system("sudo shutdown -h now")

    flash("The shutdown procedure has commenced. All Raspberry Pi functions will now stop.", "info")
    return render_template("layout.html", title="Shutdown")


@app.route('/torrents')
def torrents():
    flash("Functionality not yet implemented.", "danger")
    return render_template("layout.html", title="Torrents")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

app.secret_key = '2\x1f\xfb\xf5)7\x13=\r\x85\xdd;\x1fpBx\xce`\xd0\xa7\x86)?\xb4'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



