''' Calculates the happiest state'''
import json
import sys


def load_sentiment(senti_fh):
     '''Returns sentiment dictionary '''
     senti_dict = {}
     for line in senti_fh:
         key, value = line.split('\t')
         senti_dict[key] = value
     #print "there are %s words in this file" % len(senti_dict)
     return senti_dict

def load_states():
    '''Loads states dict '''

    states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    return states_dict

def get_place(place_dict, states_dict):
    ''''''

    state=None
    if 'country' in place_dict or 'country_code' in place_dict:  ##in US
        if place_dict['country']=='United States' or place_dict['country_code']=='US':
            place_name = place_dict['name']
            for k, v in states_dict.items():
                #print place_name, v
                if v == place_name:

                    state = k
                    break

    #print state
    return state

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



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    ##load term dictionary
    sent_dict = load_sentiment(sent_file)

    ##load states dictionary
    states_dict = load_states()
    total_states = len(states_dict)

    ##iterate
    state_sent_dict= {}
    for line in tweet_file.readlines():
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict and tweet_dict['lang']=='en': ## Only english tweets
            tweet = tweet_dict['text']
            if 'place' in tweet_dict and tweet_dict['place'] is not None:   ## Attempt #1 explicit Place declaration
                place_dict = tweet_dict['place']
                #print tweet_dict['place']
                state = get_place(place_dict, states_dict)
                if state:
                    #print state
                    ## Get sentiment
                    sent_word, state_sent = get_sentiment_metric(tweet, sent_dict)
                    ## Append to final dict
                    if state in state_sent_dict:
                        state_sent_dict[state]+=state_sent
                    else:
                        state_sent_dict[state]=state_sent

    #print state_sent_dict
    for k in sorted(state_sent_dict, key=state_sent_dict.get, reverse=True):
        #print "%s in the happiest state " % k
        print "%s " % k
        break


if __name__ == '__main__':
    main()

