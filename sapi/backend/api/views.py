from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, NoteSerializer
from .models import Note

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    query = User.objects.all() # list of all users ?
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # anyone can call this view


class ProfileUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user

    def get(self, request):
        # request.user will hold the authenticated user
        user = request.user
        return Response({'id': user.id, 'username': user.username})

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # only authenticated can call this view

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        # since author is read-only
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

        return super().perform_create(serializer)

class NoteDeleteView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
