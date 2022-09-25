from django.shortcuts import render
from bookmark.models import Folder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FolderSerializers
from folder import serializers

@api_view(['GET','POST'])
def folderListView(request):
    if request.method == 'GET':
        folders = Folder.objects.all()
        serializers = FolderSerializers(folders, many = True)
    
    if request.method == 'POST':
        serializers = FolderSerializers( data = request.data )

        if serializers.is_valid():
            serializers.save()
    
    return Response(serializers.data)

@api_view(['POST','DELETE'])
def folderUpdateDeleteView(request,pk):
    if request.method == 'POST':
        folder = Folder.objects.get( id = pk )
        serializers = FolderSerializers( instance = folder, data = request.data )

        if serializers.is_valid():
            serializers.save()
        
        return Response( serializers.data )
    
    if request.method == 'DELETE':
        folder = Folder.objects.get( id = pk)
        folder.delete()

        return Response('Folder Deleted Successfully !')