# -*- coding: utf-8 -*-
"""reddit_ingest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M5YUHoUYXVS1yDa1xAOttUH-4Fbbjaks

<a href="https://colab.research.google.com/github/atharvkaushik1910/GoQuant--Sentiment-Analysis/blob/main/reddit_ingest.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import praw
import pandas as pd

def fetch_reddit_data(subreddits, post_limit=100):
    reddit = praw.Reddit(
        client_id='n8_Bmi8dUSVm1bhwkLpjfA',
        client_secret='BvDzQQ8KKnGudFac-luVSvHHWVjLig',
        user_agent='GoQuantSentimentApp'
    )

    all_posts = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=post_limit):
            all_posts.append([subreddit_name, post.title, post.selftext, post.score])

    df = pd.DataFrame(all_posts, columns=['Subreddit', 'Title', 'Text', 'Score'])
    df.to_csv('data/reddit_posts.csv', index=False)

    print(f"Saved {len(df)} posts to data/reddit_posts.csv")
    return df