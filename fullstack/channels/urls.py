from django.urls import path
from .views import *

urlpatterns = [
    path('', channel_list, name='channel_list'),
    path('create/', create_channel, name='create_channel'),
    path('delete/<int:channel_id>/', delete_channel, name='delete_channel'),
    path('<int:channel_id>/edit/', edit_channel, name='edit_channel'),
    path('<int:channel_id>/', channel_detail, name='channel_detail'),

]
