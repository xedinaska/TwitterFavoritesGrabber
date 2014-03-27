from TweetsHandling import TweetsHandler
from TweetsHandling.Beautifier import TXTBeautifier


class TxtTweetsHandler(TweetsHandler.TweetsHandler):

    tweets_storage_file = "Favorites.txt"

    def save(self):
        beautifier = TXTBeautifier.TXTBeautifier()

        storage_file = open(self.tweets_storage_file, 'a+')

        counter = 1
        for tweet in self.favorites:
            prepared_text = beautifier.get_prepared_tweet(tweet, counter)
            storage_file.write(prepared_text.encode("utf8"))
            counter += 1

        storage_file.close()

    def set_storage_file(self, file):
        self.tweets_storage = file

        return self

    def get_storage_file(self):
        return self.tweets_storage_file