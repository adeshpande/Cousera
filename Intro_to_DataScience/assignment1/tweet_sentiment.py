'''
--Aniket Deshpande
'''

import sys
import json 

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiment(senti_fh):
    '''Returns sentiment dictionary '''
    senti_dict = {}
    for line in senti_fh:
        key, value = line.split('\t')
        senti_dict[key] = value
    #print "there are %s words in this file" % len(senti_dict)
    return senti_dict


def get_tweet_score(tweet, senti_dict):
    '''Returns score per tweet for file '''
    tweet_score = 0
    for word in tweet.split():
        if word in senti_dict:
            tweet_score += int(senti_dict[word])
    
    return tweet_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    ## load sentiment dictionary
    senti_dict = load_sentiment(sent_file)

    ## loop over tweet_file:
    for line in tweet_file.readlines():
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict and tweet_dict['lang']=='en': ## Only english tweets
            tweet = tweet_dict['text']
            tweet_score = get_tweet_score(tweet, senti_dict)
            #print "%s --> %s" % (tweet, tweet_score)
            print "%s" % (tweet_score)

    sent_file.close()
    tweet_file.close()


if __name__ == '__main__':
    main()
