from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


class NotificationManager(models.Manager):

    def get_by_user(self, request):
        return self.get_queryset().filter(user=request.user, is_active=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = NotificationManager()

    def set_seen(self):
        self.is_active = False
        self.save()

    def __str__(self) -> str:
        return self.title
