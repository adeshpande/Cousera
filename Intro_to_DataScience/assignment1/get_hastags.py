#!/usr/bin/env python

import json
import sys

i = 0
for line in sys.stdin:
    tweet_dict = json.loads(line)
    #i +=1
    #print i
    if 'entities' in tweet_dict:
        #if 'hashtags' in tweet_dict['entities'] and if tweet_dict['entities']['hashtags']:
        if tweet_dict['entities'].get('hashtags', None):
            #print tweet_dict['entities']['hashtags']
            print line

