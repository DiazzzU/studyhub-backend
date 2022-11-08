from django.urls import path
from deck.views import FolderViewSet

urlpatterns = [
    path('create/', FolderViewSet.as_view({"post": "create"}), name='folder_create'),
    path('list/', FolderViewSet.as_view({"get": "list"}), name='get_by_name')
]