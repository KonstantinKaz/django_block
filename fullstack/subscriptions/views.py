from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscription
from channels.models import Channel

def subscription_list(request):
    user = request.user
    subscriptions = Subscription.objects.filter(user=user)
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions})

def subscribe_channel(request, channel_id):
    user = request.user
    channel = get_object_or_404(Channel, id=channel_id)
    subscription = Subscription(user=user, channel=channel)
    subscription.save()
    return redirect('subscription_list')

def unsubscribe_channel(request, channel_id):
    user = request.user
    channel = get_object_or_404(Channel, id=channel_id)
    subscription = Subscription.objects.filter(user=user, channel=channel)
    subscription.delete()
    return redirect('subscription_list')
