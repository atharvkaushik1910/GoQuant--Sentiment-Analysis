# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11N9xu7Ct4ixnfN-15UkZs3ReYt96lzyN
"""

import tweepy
import pandas as pd

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMpO3AEAAAAAl%2BGUdnDjPwJzXSsZ80qLGpW3jBc%3DGPoIwrnmmqRn09xNmIlU3mYmHqBLJWK5A7NqfDoTPjxY4y9Dsf'

client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(query, max_tweets=100):
    tweets = client.search_recent_tweets(
        query=query,
        max_results=max_tweets if max_tweets <= 100 else 100,  # Tweepy API max is 100 per call
        tweet_fields=['created_at', 'lang', 'author_id', 'text']
    )

    data = []
    if tweets.data:
        for tweet in tweets.data:
            data.append([tweet.id, tweet.text, tweet.created_at, tweet.lang, tweet.author_id])

    df = pd.DataFrame(data, columns=['TweetID', 'Text', 'CreatedAt', 'Language', 'AuthorID'])
    df.to_csv('data/tweets_api.csv', index=False)
    print(f"Saved {len(df)} tweets to data/tweets_api.csv")
    return df