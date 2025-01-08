from django.urls import path

from .views import (
    home_page,
    browse_page,
    streams_page,
    game_detail,
    create_stream,
    create_clip_view,
    add_to_library,
    download_game_in_library
)

# http://127.0.0.1:8000/
urlpatterns = [
    path('', home_page, name='home'),
    path('browse/', browse_page, name='browse'),
    path('streams/', streams_page, name='streams'),
    path('streams/create/', create_stream, name='stream_create'),
    path('games/<int:pk>/', game_detail, name='detail'),
    path('clips/create/', create_clip_view, name='create_clip'),
    path('library/add/<int:game_id>/<int:user_id>/', add_to_library, name='add_to_library'),
    path('library/<int:library_item_id>/',
         download_game_in_library, name='download')
]
