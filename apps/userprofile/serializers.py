from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user",
            "follows",
        )


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "user_profile",
        )
