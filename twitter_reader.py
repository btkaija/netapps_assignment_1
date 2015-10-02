import tweepy

APP_KEY = 'i0k5jBnZh5EV80BtT4yPgjH9U'
APP_SECRET = 'loDNxg8tcFFSKghVj6FRhtsqaTecrmH2KIAdwcej3I0bwoUA13'
OAUTH_TOKEN = '2752130490-KerLqUMQt7tphPSjNICkQzQdU3Gnv7ugxaBb81M'
OAUTH_TOKEN_SECRET = 'mRfsCDdHoztDOjRmrpuV03yJQStkZZE5PAq17uV1FgmSB'

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

my_tweets = api.user_timeline('btkaija')
print my_tweets[0].text 
#for tweet in public_tweets:
#    print tweet.text
