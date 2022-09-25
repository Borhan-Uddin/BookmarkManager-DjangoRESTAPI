from django.urls import path
from . import views
urlpatterns = [
    path('', views.folderListView, name= 'folder-list'),
    path('<int:pk>/', views.folderUpdateDeleteView, name= 'folder-update-delete'),
]