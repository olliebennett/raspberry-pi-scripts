#!/usr/bin/env python
# -*- coding: utf-8

import os
import olliebennett.logger as Log
import olliebennett.twitter as Twitter

__author__ = 'Ollie Bennett | http://olliebennett.co.uk/'

# Get current CPU temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

Log.debug(Log.TEMPERATURE, temp)

status = 'My current CPU temperature is '+temp+'°C'

Log.debug(Log.TWITTER, "New Status: %s" % status)

# Update status!
Twitter.tweet(status)
