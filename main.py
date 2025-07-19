from ingestion.twitter_ingest import fetch_tweets
from ingestion.reddit_ingest import fetch_reddit_data
from ingestion.news_ingest import fetch_news_data
from ingestion.prices_ingest import fetch_prices

def run_all_ingestion():
    print("Fetching Tweets...")
    fetch_tweets("bitcoin OR crypto OR ethereum lang:en", max_tweets=1000)

    print("Fetching Reddit Posts...")
    fetch_reddit_data(['CryptoCurrency', 'Bitcoin', 'CryptoMarkets'], post_limit=100)

    print("Fetching News Headlines...")
    fetch_news_data('crypto OR bitcoin OR ethereum', pages=5, page_size=20)

    print("Fetching Market Prices...")
    fetch_prices(["BTC-USD", "ETH-USD", "SOL-USD", "AAPL", "TSLA"])

if __name__ == "__main__":
    run_all_ingestion()

