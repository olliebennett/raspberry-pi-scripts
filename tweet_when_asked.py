#!/usr/bin/env python
# -*- coding: utf-8
from olliebennett.steamers import TweetMyTemperature

if __name__ == '__main__':
    # Set the thread running!
    stream = TweetMyTemperature(handle=TwitterConfig.HANDLE, trigger='cpu_temp',
                                 api.app_key, api.app_secret, api.oauth_token,
                                 api.oauth_token_secret)
    stream.statuses.filter(track=TwitterConfig.HANDLE)
