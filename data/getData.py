from tweety import Twitter
import pandas as pd
from tweety import user
# 需求：获取某些关键词的推文，将其存储到csv文件中，包括推文的文本、日期、点赞数、转发数.




if __name__ == '__main__':
    # Default Settings : Login with session
    app = Twitter("session")
    app.sign_in("JaimeAnder55094", "xAdtrM95BnYBzVO")

    # set the keywords you want to search
    keywords = ["2024 US President Election", "Donald Trump", "Joe Biden"]

    # get the tweets and store them in a csv file
    all_tweet_info = []
    for keyword in keywords:
        tweets = app.search(keyword, 15)
        for tweet in tweets:
            tweet_info = [tweet.id, tweet.author.id, tweet.author.followers_count, tweet.author.location,
                          tweet.author.verified, tweet.text, tweet.date, tweet.likes, tweet.is_sensitive, tweet.views,
                          tweet.place, tweet.retweet_counts, tweet.reply_counts, tweet.vibe, keyword, tweet.language]
            all_tweet_info.append(tweet_info)

    df = pd.DataFrame(all_tweet_info,
                      columns=["id", "author_id", "follower_counts", "author_location", "author_verified", "text",
                               "date", "likes", "is_sensitive", "views", "place", "retweet_counts", "reply_counts",
                               "vibe", "keyword", "language"])

    print(len(df))
    # mode = 'a' means append
    df.to_csv("tweets.csv", index=False, mode='a', header=False);

    print(len(df))


