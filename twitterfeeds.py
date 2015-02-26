

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "359742951-5rYDfoul59RRHe97epz7j6ffiaKPgLaXcEgeG1zs"
access_token_secret = "jZgdDXsdjf22ck6yzLEEOlZBVxkBpHUCMVa0vJ147B1V4"
consumer_key = "XKaaACzJXk4SKrAUBtdNY4KDV"
consumer_secret = "Ypfbpfld4p6aT7qrFGZKq2uqDUaaS7Hf7HNOC4xAOHFJSaXsJ5"



class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
    	print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['@gap', '@jcrew', '@americanapparel', '@hm'])