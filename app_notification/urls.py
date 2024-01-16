from django.urls import path
from .views import notification_list_view, open_notification_view

urlpatterns = [
    path('', notification_list_view),
    path('<int:id>/', open_notification_view)
]
