from rest_framework import serializers
from bookmark.models import Folder

class FolderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'