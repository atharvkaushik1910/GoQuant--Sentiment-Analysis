{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMiK1Sa6kLj8RmEVPiyHUlI",
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
        "<a href=\"https://colab.research.google.com/github/atharvkaushik1910/GoQuant--Sentiment-Analysis/blob/main/prices_ingest.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Cr3PFcCaJ7G",
        "outputId": "8e034afe-9062-4e9a-e3f0-48c4ebe1ef82"
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
            "                                    Open           High            Low  \\\n",
            "Datetime                                                                 \n",
            "2025-07-14 00:00:00+00:00  119118.796875  119457.859375  119000.617188   \n",
            "2025-07-14 01:00:00+00:00  119117.421875  119224.375000  118961.773438   \n",
            "2025-07-14 02:00:00+00:00  119132.500000  119914.992188  119024.851562   \n",
            "2025-07-14 03:00:00+00:00  119701.515625  121178.976562  119646.640625   \n",
            "2025-07-14 04:00:00+00:00  120771.765625  121373.273438  120645.882812   \n",
            "\n",
            "                                   Close       Volume  Dividends  Stock Splits  \n",
            "Datetime                                                                        \n",
            "2025-07-14 00:00:00+00:00  119118.906250   8865234944        0.0           0.0  \n",
            "2025-07-14 01:00:00+00:00  119135.039062  10423504896        0.0           0.0  \n",
            "2025-07-14 02:00:00+00:00  119702.203125  14228422656        0.0           0.0  \n",
            "2025-07-14 03:00:00+00:00  120785.570312  20088344576        0.0           0.0  \n",
            "2025-07-14 04:00:00+00:00  121369.859375  14364160000        0.0           0.0  \n"
          ]
        }
      ],
      "source": [
        "# Stock & Crypto Prices (via yFinance)\n",
        "pip install pandas snscrape praw newsapi-python yfinance\n",
        "\n",
        "import yfinance as yf\n",
        "\n",
        "btc = yf.Ticker(\"BTC-USD\")\n",
        "btc_history = btc.history(period=\"1d\", interval=\"1h\")\n",
        "print(btc_history.head())\n",
        "\n",
        "\n"
      ]
    }
  ]
}
