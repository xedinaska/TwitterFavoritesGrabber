class TXTBeautifier:

    def get_prepared_tweet(self, tweet, position):
        tweet_text = "\n"
        tweet_text += "===================" + str(position) + "======================"
        tweet_text += "\n@" + tweet.user.screen_name + " " + tweet.user.name + " at " + str(tweet.created_at)
        tweet_text += "\n\n"
        tweet_text += tweet.text
        tweet_text += "\n========================================="
        tweet_text += "\n"

        return tweet_text
