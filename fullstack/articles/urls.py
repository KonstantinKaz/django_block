from django.urls import path
from articles.views import *
from comments.views import *
# from favorites.views import *


urlpatterns = [
    path('', article_list, name='article_list'),
    path('create/', create_article, name='create_article'),
    path('edit/<int:article_id>/', edit_article, name='edit_article'),
    path('delete/<int:article_id>/', delete_article, name='delete_article'),
    path('detail/<int:article_id>/', article_detail, name='article_detail'),
    path('comments/create/<int:article_id>/', create_comment, name='create_comment'),
    path('comments/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    # path('add_to_favorites/<int:article_id>/', add_to_favorites, name='add_to_favorites'),
    # path('favorites/', favorites_list, name='favorites_list'),
]

