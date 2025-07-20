# GoQuant--Sentiment-Analysis

# GoQuant Sentiment-Based Trading Signal System

## Overview
This project implements a **Real-Time Sentiment Analysis and Trading Signal Generation Engine** using:
- **Twitter**
- **Reddit**
- **Financial News**
- **Market Price Data (Crypto, Stocks)**

We use the **FinBERT** model, a pre-trained financial domain-specific BERT variant, for sentiment analysis.  
FinBERT specializes in identifying **Positive**, **Negative**, and **Neutral** sentiments in financial texts, enabling us to:
- **Score** each text (tweet, reddit post, news article) on a compound sentiment scale (-1 to +1).
- Aggregate these scores across sources to derive an overall **Fear & Greed Index**.

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

- **Tweets scraping**

- **Reddit scraping**

- **News API fetching**

- **Price data collection**

All results will be saved as CSVs in the **/data folder**.

### 3. Fetch Data
Fetch tweets, reddit posts & comments, news articles, and asset price data:
```
python ingestion/fetch_tweets.py
python ingestion/fetch_reddit.py
python ingestion/fetch_news.py
python ingestion/fetch_prices.py

```

### 4. Sentiment Analysis
Analyze the sentiment of the collected data using FinBERT

Run sentiment analysis on the fetched data:
```
python analysis/analyze_tweets.py
python analysis/analyze_reddit.py
python analysis/analyze_news.py

```
Outputs:

```data/tweets_sentiment.csv```

```data/reddit_sentiment.csv```

```data/news_sentiment.csv```

### 5. Aggregate Sentiments & Calculate Fear/Greed Index
Combine all sentiment data sources into a single Fear & Greed Index:
```
python analysis/aggregate_sentiment.py
```
Output:

Console output showing index value and market mood: Fearful / Neutral / Greedy.

### 6. Preprocess Market Price Data
```
python analysis/preprocess_prices.py

```

### 7. Correlate Sentiment with Price Changes
Correlate the overall sentiment score with the % price changes to understand predictive power:
```
python analysis/correlate_sentiment_price.py

```
Output:

```data/sentiment_price_correlation.csv```
It includes the correlation coefficient for each asset (BTC, ETH, etc.)

### 8. Generate Trade Signals
```
python analysis/generate_signals.py

```
Output:

Console shows:

-Latest Sentiment

-Latest Price Change

-Sentiment-Price Correlation

-Trade Signal (BUY / SELL / HOLD)

-Confidence Score

## Outputs
-**Fear & Greed Index:** Console output from ```aggregate_sentiment.py```

-**Correlation Metrics:** data/sentiment_price_correlation.csv

-**Trade Signals:** Console output from generate_signals.py showing:

-**Latest sentiment score**

-**Latest price % change**

-**Correlation value**

-**Generated trading signal (BUY / SELL / HOLD)**

-**Confidence score**


## Assets Covered
-**Bitcoin (BTC-USD)**

-**Ethereum (ETH-USD)**

-**Solana (SOL-USD)**

-**Apple (AAPL)**

-**Tesla (TSLA)**


## Future Work
-**Integrate real-time data streaming**

-**Enhance sentiment models with advanced NLP (e.g., sarcasm detection)**

-**Implement backtesting on historical data**

-**Build visualization dashboards**


## Author
Developed as part of GoQuant's Backend Sentiment Engine Assignment.
