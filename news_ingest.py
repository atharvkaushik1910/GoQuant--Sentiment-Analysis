{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNdnPq5Istzejg31CzUYJYm",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/atharvkaushik1910/GoQuant--Sentiment-Analysis/blob/main/news_ingest.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Cr3PFcCaJ7G",
        "outputId": "9c65a2a1-1757-4cc3-98ee-d089f015695f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: snscrape in /usr/local/lib/python3.11/dist-packages (0.7.0.20230622)\n",
            "Requirement already satisfied: praw in /usr/local/lib/python3.11/dist-packages (7.8.1)\n",
            "Requirement already satisfied: newsapi-python in /usr/local/lib/python3.11/dist-packages (0.2.7)\n",
            "Requirement already satisfied: yfinance in /usr/local/lib/python3.11/dist-packages (0.2.65)\n",
            "Requirement already satisfied: numpy>=1.23.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: requests[socks] in /usr/local/lib/python3.11/dist-packages (from snscrape) (2.32.3)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.11/dist-packages (from snscrape) (5.4.0)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.11/dist-packages (from snscrape) (4.13.4)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from snscrape) (3.18.0)\n",
            "Requirement already satisfied: prawcore<3,>=2.4 in /usr/local/lib/python3.11/dist-packages (from praw) (2.4.0)\n",
            "Requirement already satisfied: update_checker>=0.18 in /usr/local/lib/python3.11/dist-packages (from praw) (0.18.0)\n",
            "Requirement already satisfied: websocket-client>=0.54.0 in /usr/local/lib/python3.11/dist-packages (from praw) (1.8.0)\n",
            "Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.11/dist-packages (from yfinance) (0.0.11)\n",
            "Requirement already satisfied: platformdirs>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (4.3.8)\n",
            "Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2.4.6)\n",
            "Requirement already satisfied: peewee>=3.16.2 in /usr/local/lib/python3.11/dist-packages (from yfinance) (3.18.2)\n",
            "Requirement already satisfied: curl_cffi>=0.7 in /usr/local/lib/python3.11/dist-packages (from yfinance) (0.11.4)\n",
            "Requirement already satisfied: protobuf>=3.19.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (5.29.5)\n",
            "Requirement already satisfied: websockets>=13.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (15.0.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4->snscrape) (2.7)\n",
            "Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4->snscrape) (4.14.1)\n",
            "Requirement already satisfied: cffi>=1.12.0 in /usr/local/lib/python3.11/dist-packages (from curl_cffi>=0.7->yfinance) (1.17.1)\n",
            "Requirement already satisfied: certifi>=2024.2.2 in /usr/local/lib/python3.11/dist-packages (from curl_cffi>=0.7->yfinance) (2025.7.9)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests[socks]->snscrape) (3.4.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests[socks]->snscrape) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests[socks]->snscrape) (2.4.0)\n",
            "Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from requests[socks]->snscrape) (1.7.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.11/dist-packages (from cffi>=1.12.0->curl_cffi>=0.7->yfinance) (2.22)\n",
            "                                               Title  \\\n",
            "0     Crypto Bros Are Winning Big in Trump’s America   \n",
            "1  Bitcoin Who? Wall Street Has a New Crypto Obse...   \n",
            "2  Bitcoin Whales Are Offloading Their Bags on In...   \n",
            "3  Your Bitcoin Might Soon Get You a Mortgage—No,...   \n",
            "4  A Viral Question Is Puzzling Bitcoin Fans: Why...   \n",
            "\n",
            "                                         Description  \n",
            "0  The industry that brought you Bitcoin casinos ...  \n",
            "1  While Bitcoin hits new highs, a little-known c...  \n",
            "2  The reason the price of Bitcoin has been stuck...  \n",
            "3  The new head of the U.S. housing regulator, a ...  \n",
            "4  Corporations are buying billions, but the pric...  \n"
          ]
        }
      ],
      "source": [
        "# News Headlines (via NewsAPI)\n",
        "pip install pandas snscrape praw newsapi-python yfinance\n",
        "\n",
        "from newsapi import NewsApiClient\n",
        "\n",
        "newsapi = NewsApiClient(api_key='ef6d3ee4ee584cbaab14a9513270f3ef')\n",
        "\n",
        "top_headlines = newsapi.get_everything(q='bitcoin OR crypto',\n",
        "                                       language='en',\n",
        "                                       sort_by='relevancy',\n",
        "                                       page_size=10)\n",
        "\n",
        "news_list = []\n",
        "for article in top_headlines['articles']:\n",
        "    news_list.append([article['title'], article['description']])\n",
        "\n",
        "df_news = pd.DataFrame(news_list, columns=['Title', 'Description'])\n",
        "print(df_news.head())\n",
        "\n",
        "\n"
      ]
    }
  ]
}
