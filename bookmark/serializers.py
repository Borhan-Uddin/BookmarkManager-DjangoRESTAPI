from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Bookmark, Folder

class BookmarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'