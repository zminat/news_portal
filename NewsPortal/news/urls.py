from django.urls import path
from .views import (
   PostsList, PostDetail, SearchPostsList,
   PostCreate, PostUpdate, PostDelete,
   subscriptions,
)


urlpatterns = [
   path('news/', PostsList.as_view(), name='post_list'),
   path('news/<int:id>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', SearchPostsList.as_view(), name='search'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='post_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
