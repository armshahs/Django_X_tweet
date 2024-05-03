from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )
    # the below field helps in adding follows as well as retrieving the followers of a given user using the inverse relationship.
    # Also, symmetrical is False, because if you follow someone, then it's not necessary that they automatically follow you back.
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


# Here you are defining not just an attribute but a property.
# Properties allow you to control how a value is accessed and potentially modified when using the userprofile attribute.
# lambda function is a concise way to define a small anonymous function & u is the instance of the user object.
# get_or_create method returns a tuple containing two elements: (UserProfile instance, boolean). created (True) OR retrieved (False). We need only the first element.
User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
