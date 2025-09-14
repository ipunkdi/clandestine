"""Unit tests for social media OSINT module."""

from modules.osint.social_media import scrape_twitter


def test_scrape_twitter(monkeypatch):
    """Test scrape_twitter returns mocked tweet."""

    class MockClient:
        """Mock Tweepy client returning a tweet."""

        def search_recent_tweets(self, *_args, **_kwargs):
            """Return a mocked tweets object with one tweet."""

            class MockTweets:
                """Mock Tweets container with one tweet."""
                data = [type("Tweet", (), {"text": "mock tweet"})]

            return MockTweets()

    # Replace tweepy.Client with MockClient
    monkeypatch.setattr("tweepy.Client", MockClient)

    tweets = scrape_twitter("test")
    assert tweets == ["mock tweet"]


def test_scrape_twitter_no_results(monkeypatch):
    """Test scrape_twitter returns empty list if no tweets found."""

    class MockClient:
        """Mock Tweepy client returning no results."""

        def search_recent_tweets(self, *_args, **_kwargs):
            """Return a mocked tweets object with no data."""

            class MockTweets:
                """Mock Tweets container with no data."""
                data = None

            return MockTweets()

    monkeypatch.setattr("tweepy.Client", MockClient)

    tweets = scrape_twitter("nothing")
    assert tweets == []
