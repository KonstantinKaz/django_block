from django.urls import path
from .views import *

urlpatterns = [
    path('', subscription_list, name='subscription_list'),
    path('subscribe/<int:channel_id>/', subscribe_channel, name='subscribe_channel'),
    path('unsubscribe/<int:channel_id>/', unsubscribe_channel, name='unsubscribe_channel'),
]
