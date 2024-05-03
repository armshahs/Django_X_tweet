from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response


from .models import Tweet
from .serializers import TweetSerializer


# Create your views here.
@api_view(["POST"])
def create_tweet(request):
    serializer = TweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_all_tweets(request):
    # Adding search and if no search is specified, then add a default empty value.
    search = request.GET.get("search", "")
    tweets = Tweet.objects.all().filter(body__icontains=search)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


# Get tweets from users you follow
@api_view(["GET"])
def get_follows_tweets(request):
    userids = [request.user.id]
    # Adding search and if no search is specified, then add a default empty value.
    search = request.GET.get("search", "")

    for i in request.user.userprofile.follows.all():
        userids.append(i.user.id)

    tweets = Tweet.objects.filter(created_by_id__in=userids, body__icontains=search)

    serializer = TweetSerializer(tweets, many=True)
    return Response({"tweets": serializer.data})


@api_view(["GET"])
def search(request):
    query = request.data.get("query")
