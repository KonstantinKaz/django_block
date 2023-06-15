from django.shortcuts import render, redirect, get_object_or_404
from .models import Channel
from .forms import ChannelForm

def channel_list(request):
    channels = Channel.objects.all()
    return render(request, 'channels/channel_list.html', {'channels': channels})



def create_channel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('channel_list')  # Перенаправление на список каналов или другую страницу
    else:
        form = ChannelForm()

    return render(request, 'channels/create_channel.html', {'form': form})


def delete_channel(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    channel.delete()
    return redirect('channel_list')  # Redirect to the channel list or another page


def edit_channel(request, channel_id):
    channel = get_object_or_404(Channel, pk=channel_id)

    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('channel_list')  # Redirect to the list of channels or another page
    else:
        form = ChannelForm(instance=channel)

    return render(request, 'channels/edit_channel.html', {'form': form, 'channel': channel})