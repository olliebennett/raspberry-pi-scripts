#!/usr/bin/env python
# -*- coding: utf-8
from olliebennett.config import twitter as TwitterConfig
from olliebennett.streamers import TweetMyTemperature

if __name__ == '__main__':
    # Set the thread running!
    stream = TweetMyTemperature(TwitterConfig.HANDLE, 'cpu_temp',
                             TwitterConfig.CONSUMER_KEY, TwitterConfig.CONSUMER_SECRET,
                             TwitterConfig.ACCESS_TOKEN, TwitterConfig.ACCESS_TOKEN_SECRET)
    stream.statuses.filter(track='twitter')
