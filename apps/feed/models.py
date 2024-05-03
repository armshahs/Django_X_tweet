import uuid
from django.db import models

from django.contrib.auth.models import User
from django.utils.timesince import timesince


# Create your models here.
class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="tweets", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return str(self.created_by) + " - " + str(self.created_at)
