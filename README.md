# GoQuant--Sentiment-Analysis

# GoQuant Sentiment-Based Trading Signal System

## Overview
This project implements a **Real-Time Sentiment Analysis and Trading Signal Generation Engine** using:
- **Twitter**
- **Reddit**
- **Financial News**
- **Market Price Data (Crypto, Stocks)**

The system calculates a **Fear & Greed Index**, correlates sentiment with asset prices, and generates actionable **Buy, Sell, or Hold signals** with confidence scoring.

---

## Project Structure
``` 
├─ README.md
├─ analysis
│  ├─ 1
│  ├─ aggregate_sentiment.py
│  ├─ analyze_news.py
│  ├─ analyze_reddit.py
│  ├─ analyze_tweets.py
│  ├─ correlate_sentiment_price.py
│  ├─ generate_signals.py
│  └─ sentiment.py
├─ data
│  ├─ 1
│  ├─ news_headlines.csv
│  ├─ news_sentiment.csv
│  ├─ prices
│  │  ├─ 1
│  │  ├─ AAPL_price.csv
│  │  ├─ BTC-USD_price.csv
│  │  ├─ ETH-USD_price.csv
│  │  ├─ SOL-USD_price.csv
│  │  └─ TSLA_price.csv
│  ├─ reddit_posts.csv
│  ├─ reddit_sentiment.csv
│  ├─ tweets_api.csv
│  └─ tweets_sentiment.csv
├─ ingestion
│  ├─ news_ingest.py
│  ├─ prices_ingest.py
│  ├─ reddit_ingest.py
│  ├─ twitter_ingest.py
│  └─ x
├─ main.py
├─ preprocessing
│  ├─ 1
│  └─ preprocess_price_data.py
└─ requirements.txt
```

## Steps to run the project

### 1. Install Requirements
```
pip install -r requirements.txt
```

### 2. Run the main  script
```
python main.py
```
This will trigger:

-Tweets scraping
-Reddit scraping
-News API fetching
-Price data collection
