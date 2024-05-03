from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response


from .forms import SignupForm, UserProfile
from .models import UserProfile
from .serializers import *


# Create your views here.
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    message = "User is successfully signed up"

    form = SignupForm(request.data)
    if form.is_valid():
        user = form.save()
        user.is_active = True
        user.save()

        return Response({"message": message})
    else:
        return Response(form.errors)


# View to get details of userprofile
@api_view(["GET"])
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)
