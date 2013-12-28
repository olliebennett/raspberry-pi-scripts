from twython import TwythonStreamer
from olliebennett.tweets import tweet_cpu_temp
import olliebennett.logger as Log


class TweetMyTemperature(TwythonStreamer):
    """
        Simple streamer to tweet the pi's cpu temp when asked for it.

        i.e. @RASPBERRY_PI, what's your cpu_temp?
    """
    def __init__(self, handle, trigger='cpu_temp', *args, **kwargs):
        self.handle = handle
        self.trigger = trigger
        Log.debug(Log.TWITTER, "Starting Twitter stream monitor thread.")
        super(TweetMyTemperature, self).__init__(*args, **kwargs)

    def on_success(self, data):
        tweet = data.get('text', False)
        Log.debug(Log.TWITTER, "Received tweet: '%s'." % tweet)
        if tweet and '@%s' % self.handle in tweet and self.trigger in tweet:
            Log.debug(Log.TWITTER, "Tweet command '%s' identified! Tweeting..." % self.trigger)
            # Tweet the cpu tmp!
            # Perhaps this would be better used as a reply to the person
            # sending the tweet?
            tweet_cpu_temp()
        else:
            Log.debug(Log.TWITTER, "No valid command identified in tweet.")

    def on_error(self, status_code, data):
        Log.error(Log.TWITTER, "Error #%s" % status_code)

        # Stop trying to get data
        self.disconnect()