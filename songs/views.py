from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album


class SongView(GenericAPIView, ListModelMixin, CreateModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination

    def get(self, request, pk):
        return self.list(request, album_id=pk)

    def post(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        request.data["album_id"] = album.pk

        return self.create(request)
