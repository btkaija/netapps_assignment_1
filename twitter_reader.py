import tweepy
import socket

APP_KEY = 'i0k5jBnZh5EV80BtT4yPgjH9U'
APP_SECRET = 'loDNxg8tcFFSKghVj6FRhtsqaTecrmH2KIAdwcej3I0bwoUA13'
OAUTH_TOKEN = '2752130490-KerLqUMQt7tphPSjNICkQzQdU3Gnv7ugxaBb81M'
OAUTH_TOKEN_SECRET = 'mRfsCDdHoztDOjRmrpuV03yJQStkZZE5PAq17uV1FgmSB'

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
new_tweet = ''

def send_ack_tweet():
    print 'sending ack tweet....'

size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    my_tweets = api.user_timeline('btkaija')
    last_tweet = new_tweet
    new_tweet =  my_tweets[0].text
    if(last_tweet != new_tweet):
        print 'New Tweet Recieved! Checking format...'
        #correct format: #ECE4564_192_168_1_1_50000_LEDON
        hashtag = new_tweet.split('_')
        print 'New Tweet: ', new_tweet
        if(hashtag[0]=='#ECE4564'):
            try:
                ip = hashtag[1]+'.'+hashtag[2]+'.'+hashtag[3]+'.'+hashtag[4]
                port = hashtag[5]
                command = hashtag[6]
                #s.connect((ip,port))
                #s.send(command)
                #data = s.recv(size)
                #s.close()

                send_ack_tweet()
            except Exception, e:
                print e
                print 'Incorrect tweet format. Not sending socket comm.'
        else:
            print 'Format error: No ECE4564 hashtag found.'
#for tweet in public_tweets:
#    print tweet.text
