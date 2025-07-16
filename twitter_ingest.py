{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNz/ILQW2X0H++XWvZvGK8Z",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/atharvkaushik1910/GoQuant--Sentiment-Analysis/blob/main/twitter_ingest.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e8-K2UmA9ZE_",
        "outputId": "3e3cba72-429e-48a6-9b26-4876f17927ff"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: tweepy in /usr/local/lib/python3.11/dist-packages (4.15.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: oauthlib<4,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from tweepy) (3.3.1)\n",
            "Requirement already satisfied: requests<3,>=2.27.0 in /usr/local/lib/python3.11/dist-packages (from tweepy) (2.32.3)\n",
            "Requirement already satisfied: requests-oauthlib<3,>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from tweepy) (2.0.0)\n",
            "Requirement already satisfied: numpy>=1.23.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27.0->tweepy) (3.4.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27.0->tweepy) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27.0->tweepy) (2.4.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27.0->tweepy) (2025.7.9)\n"
          ]
        }
      ],
      "source": [
        "pip install tweepy pandas"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import tweepy\n",
        "import pandas as pd\n",
        "\n",
        "bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMpO3AEAAAAAl%2BGUdnDjPwJzXSsZ80qLGpW3jBc%3DGPoIwrnmmqRn09xNmIlU3mYmHqBLJWK5A7NqfDoTPjxY4y9Dsf'\n",
        "\n",
        "client = tweepy.Client(bearer_token=bearer_token)\n",
        "\n",
        "def fetch_tweets_via_api(query, max_results=100):\n",
        "    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['created_at', 'lang', 'author_id', 'text'])\n",
        "\n",
        "    data = []\n",
        "    for tweet in tweets.data:\n",
        "        data.append([tweet.id, tweet.text, tweet.created_at, tweet.lang, tweet.author_id])\n",
        "\n",
        "    df = pd.DataFrame(data, columns=['TweetID', 'Text', 'CreatedAt', 'Language', 'AuthorID'])\n",
        "    df.to_csv('tweets_api.csv', index=False)\n",
        "    return df\n",
        "\n",
        "query = \"bitcoin OR ethereum OR crypto lang:en\"\n",
        "df_api_tweets = fetch_tweets_via_api(query, max_results=100)\n",
        "print(df_api_tweets.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7P6F1Lgn9rL7",
        "outputId": "6571ebb2-eeff-46d4-f5d8-639260d1d4c0"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               TweetID                                               Text  \\\n",
            "0  1945163011552890968  RT @rovercrc: 💥BREAKING:\\n\\nTrump says \"digita...   \n",
            "1  1945163011502518691  RT @Crypto_Briefing: 🇺🇸 BREAKING: President Tr...   \n",
            "2  1945163011200557526  RT @Bruce_LeVell: HAPPY CRYPTO WEEK! The House...   \n",
            "3  1945163010781405195  RT @missjefa: 💲1️⃣5️⃣0️⃣ | 4️⃣ DAYS [JF316]\\n\\...   \n",
            "4  1945163010525302960  @gringolocomatt Click on my invite link 🔗 belo...   \n",
            "\n",
            "                  CreatedAt Language             AuthorID  \n",
            "0 2025-07-15 16:46:15+00:00       en  1221585514408697856  \n",
            "1 2025-07-15 16:46:15+00:00       en  1881350493869371392  \n",
            "2 2025-07-15 16:46:15+00:00       en   885677670628970497  \n",
            "3 2025-07-15 16:46:15+00:00       en  1908893665411698689  \n",
            "4 2025-07-15 16:46:15+00:00       en           2845471086  \n"
          ]
        }
      ]
    }
  ]
}
