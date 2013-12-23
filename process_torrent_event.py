#!/usr/bin/env python
# -*- coding: utf-8

"""
Process Torrent Events.
This script should be configured in the Deluge "Execute" plugin, or similar.

/path/to/process_torrent_event.py <event_type>

For example:
/home/pi/process_torrent_event.py completed

See 'recognised_events' list below for available event_type values.
"""
import sys
import olliebennett.logger as Log
import olliebennett.twitter as Twitter

__author__ = 'Ollie Bennett | http://olliebennett.co.uk/'

# Possible events
recognised_events = ["completed", "added"]

if len(sys.argv) != 5:
    Log.error(Log.TORRENT, "Invalid arguments supplied (expected {0}): {1}".format(len(sys.argv), "|".join(sys.argv)))
    sys.exit()

event_type = sys.argv[1]

if event_type not in recognised_events:
    Log.error(Log.TORRENT, "Unrecognised event type '{event_type}' specified - use one of: {recognised_events}."
              .format(event_type=event_type, recognised_events="|".join(recognised_events)))
    sys.exit()

# Note: these are usually argv[1:3] but we have configured the event type as first parameter.
torrent_id = sys.argv[2]
torrent_name = sys.argv[3]
save_path = sys.argv[4]

# Log the event
log_message = "Torrent {event_type}: ID:'{torrent_id}', Name:'{torrent_name}', SavePath:'{save_path}'."\
    .format(event_type=event_type, torrent_id=torrent_id, torrent_name=torrent_name, save_path=save_path)
Log.debug(Log.TORRENT, log_message)

# Update status!
status = "Torrent {event_type}: {torrent_name}".format(event_type=event_type, torrent_name=torrent_name)
Twitter.tweet(status)
