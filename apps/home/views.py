from django.shortcuts import render, redirect

from . import models
from .forms import StreamForm, ClipForm
from django.contrib.auth.models import User





def home_page(request):
    games = models.Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'home/index.html', context)


def browse_page(request):
    return render(request, 'home/browse.html')


def streams_page(request):
    streams = models.Stream.objects.all()
    games = models.Game.objects.all()

    context = {
        'streams': streams,
        'games': games
    }
    return render(request, 'home/streams.html', context)


def game_detail(request, pk):
    game = models.Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'home/detail.html', context)


def create_stream(request):
    if request.method == 'POST':
        form = StreamForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('streams')
    else:
        form = StreamForm()

    context = {
        'form': form
    }
    return render(request, 'home/stream_form.html', context)

def create_clip_view(request):
    if request.method == 'POST':
        form = ClipForm()
    else:
        form = ClipForm()

    context = {
        'form': form
    }
    return render(request, 'home/clip_form.html', context)


def add_to_library(request, game_id, user_id):
    user = User.objects.get(pk=user_id)
    game = models.Game.objects.get(pk=game_id)

    library, created = models.Library.objects.get_or_create(
        user=user
    )

    item, item_created = models.LibraryItem.objects.get_or_create(
        library=library,
        game=game
    )

    return redirect('profile')


def download_game_in_library(request, library_item_id):
    item = models.LibraryItem.objects.get(pk=library_item_id)
    item.is_downloaded = not item.is_downloaded

    item.save()
    return redirect('profile')
