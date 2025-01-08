from django.urls import path

from .views import (
    profile_page,
    login_view,
    registration_view,
    user_logout,
    edit_profile
)

urlpatterns = [
    path('', profile_page, name='profile'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', user_logout, name='logout'),
    path('<int:pk>/edit/', edit_profile, name='edit')
]
