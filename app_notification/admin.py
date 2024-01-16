from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user=request.user)

    def save_model(self, request, obj, form, change) -> None:
        obj.user = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Notification, NotificationAdmin)
