from django.urls import path
from .views import NewsList, PostDetail


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:id>', PostDetail.as_view()),
]