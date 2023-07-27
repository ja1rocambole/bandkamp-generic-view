from rest_framework import serializers

from .models import Song
from albums.models import Album


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), source="album"
    )

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
