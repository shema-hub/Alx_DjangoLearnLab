from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer, FollowSerializer, UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
     
    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "email": user.email,
            "bio": user.bio,
            "profile_picture": user.profile_picture,
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data  # Now this is a user object
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": {
                    "id": user.id,
                    "email": user.email,
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowViewSet(viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    
    @action(detail=False, methods=['post'])
    def follow(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = get_object_or_404(CustomUser, id=serializer.validated_data['user_id'])
        
        if request.user.follow(user):
            return Response({'status': 'following'}, status=status.HTTP_200_OK)
        return Response({'error': 'Already following or invalid user'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def unfollow(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = CustomUser.objects.get(id=serializer.validated_data['user_id'])
        
        if request.user.unfollow(user):
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not following or invalid user'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def profile(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    success = request.user.follow(target_user)  # Uses the model's follow() method
    if success:
        return Response({"status": "success", "message": f"Followed {target_user.email}"})
    return Response({"status": "failed", "message": "Already following or invalid action"}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    success = request.user.unfollow(target_user)  # Uses the model's unfollow() method
    if success:
        return Response({"status": "success", "message": f"Unfollowed {target_user.email}"})
    return Response({"status": "failed", "message": "Not following or invalid action"}, status=400)