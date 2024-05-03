from django.urls import path, include

from .views import create_tweet, get_all_tweets, get_follows_tweets

urlpatterns = [
    path("create_tweet/", create_tweet, name="create_tweet"),
    path("get_all_tweets/", get_all_tweets, name="get_all_tweets"),
    # See tweets from people whom you follow.
    path("get_follows_tweets/", get_follows_tweets, name="get_follows_tweets"),
]
