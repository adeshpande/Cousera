#!/usr/bin/env python

'''Prints top ten uniq hastags '''

import json
import sys


def main():
    tweet_file = open(sys.argv[1])

    ## hashtagd count
    hash_dict={}

    ##iterate
    for line in tweet_file.readlines():
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict and tweet_dict['lang']=='en': ## Only english tweets
            tweet = tweet_dict['text']
            #print tweet_dict['entities']
            if 'entities' in tweet_dict and tweet_dict['entities'].get('hashtags', None):    ## if contains hastag
                #print tweet_dict['entities']['hastag']
                for hashtags in tweet_dict['entities']['hashtags']:     ## this is  a list of hashtags
                    ## increment counter here in memory
                    hashtag_text = hashtags['text']
                    if hashtag_text in hash_dict:
                        hash_dict[hashtag_text]+=1
                    else:
                        hash_dict[hashtag_text]=1

    ## sort and print
    count = 0
    for k in sorted(hash_dict, key=hash_dict.get, reverse=True):
        if count<11:
            print "%s %s " % (k, hash_dict[k])
            count+=1
        else:
            break

if __name__=="__main__":
    main()
