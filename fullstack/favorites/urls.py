from django.urls import path
# from articles.views import *
# from comments.views import *
from .views import *


urlpatterns = [
    path('', favorites_list, name='favorites_list'),
    path('add_to_favorites/<int:article_id>/', add_to_favorites, name='add_to_favorites'),
]

