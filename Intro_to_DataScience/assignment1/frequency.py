''' Calcultes term Freq from Twitter data'''


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
     print "there are %s words in this file" % len(senti_dict)
     return senti_dict

def get_sentiment_metric(tweet, sent_dict):
    '''Returns sentiment_metric for one word per tweet '''
    pos_count = 0
    neg_count = 0
    sent_metric = 0
    words = tweet.split()
    num_words = len(words)
    for word in words:
        ## known sentiments
        ## convert to lowercase
        word_key = word.lower()
        if word_key in sent_dict:
            #print sent_dict[word]
            if int(sent_dict[word_key]) > 0:
                pos_count += 1
            elif int(sent_dict[word_key]) < 0:
                neg_count += 1
        else:   ## Unknown words
            sent_word = word ## pick random word perhaps ??

    #print "%s => %s %s" % (tweet, pos_count, neg_count)

    sent_prop = float(pos_count)/(float(neg_count)+1)

    return sent_word,sent_prop



def get_term_dict(tweet_fh):
    '''Returns term dict '''
    term_dict = {}

    for line in tweet_fh.readlines():
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict and tweet_dict['lang']=='en': ## Only english tweets
            tweet = tweet_dict['text']
            for word in tweet.split():
                if not word.startswith(('@','http','RT')):   ## ignore stuff
                    if word in term_dict:
                        term_dict[word] +=1
                    else:
                        term_dict[word] = 1

    return term_dict


def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    ##load term dictionary
    term_dict = get_term_dict(tweet_file)

    ##iterate over term dict
    total_terms =len(term_dict)
    for key,value in term_dict.items():
        prop = float(value)/float(total_terms)
        print "%s %s" % (key,prop)


if __name__ == '__main__':
    main()
