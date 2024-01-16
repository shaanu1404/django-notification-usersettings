from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .models import Notification


@api_view(['GET'])
def notification_list_view(request):
    notifications = Notification.objects.get_by_user(request)
    serializer = NotificationSerializer(notifications, many=True)
    if not serializer.is_valid:
        return Response({'message': 'Failed'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def open_notification_view(request, id):
    notifications = Notification.objects.filter(
        id=id, user=request.user, is_active=True)
    if not notifications.exists():
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    notification = notifications[0]
    serializer = NotificationSerializer(notification)
    if not serializer.is_valid:
        return Response({'message': 'Failed'}, status=status.HTTP_404_NOT_FOUND)
    notification.set_seen()
    return Response(serializer.data, status=status.HTTP_200_OK)
