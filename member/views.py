from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .serializers import StaffSerializer
from .models import Staff

@api_view(['POST'])
@permission_classes([AllowAny])
def staff_registration_view(request):
    if request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def staff_login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def staff_logout_view(request):
#     logout(request)
#     return Response(status=status.HTTP_200_OK)


# Create your views here.
