import tweepy


class TwiFavoritesGrabber:

    TWEETS_COUNT = 200

    api = None

    def __init__(self, auth):
        self.api = tweepy.API(auth)

    def grab(self):

        favorites = tweepy.Cursor(self.api.favorites, count=self.TWEETS_COUNT).items()
        counter = 0

        for tweet in favorites:
            print("===================" + str(counter) + "======================")
            print("@" + tweet.user.screen_name + " " + tweet.user.name + " at " + str(tweet.user.created_at))
            print("")
            print(tweet.text.encode('utf8'))
            print("=========================================")
            print("")
            counter += 1