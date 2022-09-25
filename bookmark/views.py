from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Folder, Bookmark
from .serializers import BookmarkSerializers

@api_view(['GET','POST'])
def bookmarkListView(request):
    if request.method == 'GET':
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializers(bookmarks, many = True)
    
    if request.method == 'POST':
        serializer = BookmarkSerializers( data = request.data)

        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def folderbookmarkListView(request,pk):
    bookmarks_of_folder = Bookmark.objects.filter(folder_id__id = pk)
    serializer = BookmarkSerializers(bookmarks_of_folder, many = True)

    return Response(serializer.data)

@api_view(['POST','DELETE'])
def bookmarkUpdateDeleteView(request,pk):
    if request.method == 'POST':
        bookmark = Bookmark.objects.get(id = pk)
        serializer = BookmarkSerializers(instance = bookmark, data = request.data )

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    if request.method == 'DELETE':
        bookmark = Bookmark.objects.get(id = pk)
        bookmark.delete()

        return Response('Item successfully deleted !')
        

