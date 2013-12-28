from twython import TwythonStreamer
from olliebennett.tweets import tweet_cpu_temp

class TweetMyTemperature(TwythonStreamer):
    '''
        Simple streamer to tweet the pi's cpu temp when asked for it.

        i.e. @RASPERRY_PI, what's your cpu_temp?
    '''
    def __init__(self, handle, trigger='cpu_temp', *args, **kwargs):
        self.handle = handle
        self.trigger = trigger
        super(TweetMyTemperature, self).__init__(*args, **kwargs)

    def on_success(self, data):
        tweet = data.get('text', False)
        if tweet and '@%s' % self.handle in tweet and self.trigger in tweet:
                # Tweet the cpu tmp!
                # Perhaps this would be better used as a reply to the person
                # sending the tweet?
                tweet_cpu_temp()
