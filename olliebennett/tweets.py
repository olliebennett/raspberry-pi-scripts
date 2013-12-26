import os
import sys
import olliebennett.logger as Log
import olliebennett.twitter as Twitter

def tweet_cpu_temp():
    ''' Tweet the temperature of the cpu '''
    # Get current CPU temperature
    cmd = '/opt/vc/bin/vcgencmd measure_temp'
    line = os.popen(cmd).readline().strip()
    try:
        temp = line.split('=')[1].split("'")[0]
    except IndexError:
        log_message = "Failed to determine CPU temperature using command '{0}'.".format(cmd)
        Log.error(Log.TEMPERATURE, log_message)
        Twitter.tweet("Error: " + log_message)
        sys.exit()

    Log.debug(Log.TEMPERATURE, "T=" + temp)

    status = 'My current CPU temperature is ' + temp + '°C'

    # Update status!
    Twitter.tweet(status)
