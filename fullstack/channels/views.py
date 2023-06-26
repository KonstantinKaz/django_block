from django.shortcuts import render, redirect, get_object_or_404
from .models import Channel
from .forms import ChannelForm
from articles.models import Article
from django.contrib.auth.decorators import login_required



# Остальные представления остаются без изменений

def channel_list(request):
    channels = Channel.objects.all()
    return render(request, 'channels/channel_list.html', {'channels': channels})


@login_required
def create_channel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.owner = request.user
            channel.save()
            return redirect('channel_list')
    else:
        form = ChannelForm()
    return render(request, 'channels/create_channel.html', {'form': form})


def delete_channel(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    channel.delete()
    return redirect('channel_list')


def edit_channel(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)

    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('channel_list')
    else:
        form = ChannelForm(instance=channel)

    return render(request, 'channels/edit_channel.html', {'form': form, 'channel': channel})



def channel_detail(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    articles = Article.objects.filter(channel=channel)  # Получаем все статьи, принадлежащие каналу
    return render(request, 'channels/channel_detail.html', {'channel': channel, 'articles': articles})

