from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from django.db.models import Q

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response


class NotificationMarkAsReadView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def patch(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.mark_single_as_read(request, *args, **kwargs)
        return self.mark_all_as_read(request, *args, **kwargs)

    def mark_single_as_read(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)

    def mark_all_as_read(self, request, *args, **kwargs):
        updated_count = self.get_queryset().filter(read=False).update(read=True)
        return Response({
            'status': f'{updated_count} notifications marked as read'
        })


class UnreadNotificationCountView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        count = Notification.objects.filter(
            recipient=request.user,
            read=False
        ).count()
        return Response({'unread_count': count})