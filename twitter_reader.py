import tweepy
import socket
import time

APP_KEY = 'i0k5jBnZh5EV80BtT4yPgjH9U'
APP_SECRET = 'loDNxg8tcFFSKghVj6FRhtsqaTecrmH2KIAdwcej3I0bwoUA13'
OAUTH_TOKEN = '2752130490-KerLqUMQt7tphPSjNICkQzQdU3Gnv7ugxaBb81M'
OAUTH_TOKEN_SECRET = 'mRfsCDdHoztDOjRmrpuV03yJQStkZZE5PAq17uV1FgmSB'

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
new_tweet = api.user_timeline('btkaija')[0].text

#sends an acknowledgement tweet to @VTNetApps
def send_ack_tweet(original_hashtag, sender):
    date = time.ctime()
    print 'Sending Acknowledgement Tweet....'
    api.update_status(sender + ' Operation performed on '+date +' #' + original_hashtag)
    print 'Process complete'

size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while 1:
    my_tweets = api.user_timeline('btkaija')
    last_tweet = new_tweet
    new_tweet =  my_tweets[0].text
    if(last_tweet != new_tweet and 'Operation performed on ' not in new_tweet):
        print 'New Tweet Recieved! Checking format...'
        #correct format: @btkaija hello world!  #ECE4564_192_168_1_1_50000_LEDON
        tweet_attr = new_tweet.split('#')
        
        full_hashtag = 'NONE'
        
        for word in tweet_attr:
            #print word[0:7]
            if word[0:7] == 'ECE4564':
                full_hashtag = word
        
        #successful tweet!
        if(full_hashtag != 'NONE'):
            hashtag = full_hashtag.split('_')
            print 'New Command: ', new_tweet

            try:
                ip = hashtag[1]+'.'+hashtag[2]+'.'+hashtag[3]+'.'+hashtag[4]
                port =int(hashtag[5])
                command = hashtag[6].strip()
                print 'Correct format found. Sending socket comm.'
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(command)
                data = 'SUCCESS'
                data = s.recv(size)
                s.close()
                if data == 'SUCCESS':
                    sender = '@'+ my_tweets[0].author.screen_name
                    print 'Tweet ACK being sent to: '+sender
                    send_ack_tweet(full_hashtag, sender)
                elif data == 'FAIL':
                    print 'Unsuccessful operation'
                else:
                    print 'Unrecognized response from server'

            except Exception, e:
                print e
                print 'Incorrect tweet format. Not sending socket comm.'
        else:
            print 'Incorrect tweet format. Not sending socket comm.'

    #this limits the querey time to less than 180 every 15 minutes which defined by twitter
    print 'Waiting for new tweet...'
    time.sleep(6)

#end
