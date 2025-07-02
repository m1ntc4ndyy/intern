from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import isOwnerOrReadOnly
from django.contrib.auth.models import User
# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer