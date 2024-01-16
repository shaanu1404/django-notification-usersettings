from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserAppSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(
        Theme, on_delete=models.SET_DEFAULT, default="light")

    def __str__(self):
        return self.user.email
