
from django.urls import path
from . import views
urlpatterns = [
    path('', views.bookmarkListView, name= 'bookmark-list'),
    path('folders/<int:pk>/',views.folderbookmarkListView, name='folderwise-bookmark'),
    path('<int:pk>/', views.bookmarkUpdateDeleteView, name= 'delete-update-bookmark'),
]
