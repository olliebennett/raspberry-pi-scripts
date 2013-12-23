__author__ = 'Ollie Bennett | http://olliebennett.co.uk/'

import olliebennett.logger as Log
import olliebennett.config.twitter as TwitterConfig
from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError

# Get Twitter API
api = Twython(TwitterConfig.CONSUMER_KEY,
              TwitterConfig.CONSUMER_SECRET,
              TwitterConfig.ACCESS_TOKEN,
              TwitterConfig.ACCESS_TOKEN_SECRET)


def tweet(status):

    if len(status) > 140:
        Log.warn(Log.TWITTER, "Trimming long tweet (total {0} chars): '{1}'.".format(len(status), status))
        status = status[:137] + "..."

    try:
        Log.info(Log.TWITTER, "Updating status: '{0}' (total {1} chars).".format(status, len(status)))
        api.update_status(status=status)
    except TwythonAuthError as tae:
        Log.error(Log.TWITTER, "Authentication error: " + str(tae))
    except TwythonRateLimitError as trle:
        Log.error(Log.TWITTER, "Rate limit error: " + str(trle))
    except TwythonError as te:
        Log.error(Log.TWITTER, "Failed to update status: " + str(te))