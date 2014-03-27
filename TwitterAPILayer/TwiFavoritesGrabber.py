import tweepy


class TwiFavoritesGrabber:

    TWEETS_COUNT = 200

    api = None

    def __init__(self, auth):
        self.api = tweepy.API(auth)

    def grab(self):
        favorites = tweepy.Cursor(self.api.favorites, count=self.TWEETS_COUNT).items()

        return favorites