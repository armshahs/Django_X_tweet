from rest_framework import serializers

from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        read_only_fields = ("created_by",)
        fields = (
            "id",
            "body",
            "created_by",
            "created_at_formatted",
        )
