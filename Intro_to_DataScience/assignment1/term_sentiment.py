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
    for word in tweet.split():
        ## known sentiments
        if word in sent_dict:
            if sent_dict[word] > 0:
                pos_count += 1
            elif sent_dict[word] < 0:
                neg_count += 1 
        else:## Unknown words
            sent_word = word ## pick random word perhaps ?? 
    
    if neg_count!=0:
        sent_metric = float(pos_count)/float(neg_count)

    return sent_word,sent_metric


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    ##load sent dictionary
    sent_dict = load_sentiment(sent_file)

    for line in tweet_file.readlines():
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict and tweet_dict['lang']=='en': ## Only english tweets         
            tweet = tweet_dict['text']
            sent_word, sent_metric = get_sentiment_metric(tweet, sent_dict)    
            print "%s, %s" % (sent_word, sent_metric)
        

if __name__ == '__main__':
    main()
