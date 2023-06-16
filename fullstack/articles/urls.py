# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('channels/<int:channel_id>/', views.channel_articles, name='channel_articles'),
#     path('create/<int:channel_id>/', views.create_article, name='create_article'),
#     path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
#     path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.create_article, name='create_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]
