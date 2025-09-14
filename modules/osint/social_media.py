"""
Module for social media OSINT collection using Twitter API.
"""

import tweepy
from core.config.loader import load_config

def scrape_twitter(keyword: str) -> list[str]:
    """
    Search recent tweets based on a keyword using the Twitter API v2.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        list[str]: A list of tweet texts.
    """
    config = load_config()
    client = tweepy.Client(bearer_token=config.twitter_bearer_token)
    response = client.search_recent_tweets(query=keyword, max_results=10)

    if not response.data:
        return []
    return [tweet.text for tweet in response.data]
