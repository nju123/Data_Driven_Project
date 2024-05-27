import tweety
import pandas  as pd
from tweety import Twitter
from tweety import user

def fetch_data():
    # Default Settings : Login with session
    app = Twitter("session")
    app.sign_in("JaimeAnder55094", "xAdtrM95BnYBzVO")

    # set the keywords you want to search
    keywords = ["Donald Trump", "Joe Biden"]

    # get the tweets and store them in a csv file
    all_tweet_info = []
    for keyword in keywords:
        tweets = app.search(keyword, 1)
        for tweet in tweets:
            tweet_info = [tweet.id, tweet.author.id, tweet.author.followers_count, tweet.author.location,
                          tweet.author.verified, tweet.text, tweet.date, tweet.likes, tweet.is_sensitive, tweet.views,
                          tweet.place, tweet.retweet_counts, tweet.reply_counts, tweet.vibe, keyword, tweet.language]
            all_tweet_info.append(tweet_info)

    df = pd.DataFrame(all_tweet_info,
                      columns=["id", "author_id", "follower_counts", "author_location", "author_verified", "text",
                               "date", "likes", "is_sensitive", "views", "place", "retweet_counts", "reply_counts",
                               "vibe", "keyword", "language"])
    df.to_csv("current_data.csv", index=False)
    return

