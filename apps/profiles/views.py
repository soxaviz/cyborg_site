from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def profile_page(request):
    return render(request, 'profiles/profile.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'profiles/login.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form = form.save()
            profile = UserProfile.objects.create(
                user=form
            )
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'profiles/registration.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def edit_profile(request, pk):
    user = request.user
    profile = UserProfile.objects.get(pk=pk)

    if request.method == "POST":
        data = request.POST
        files = request.FILES

        user.username = data['username']
        user.save()

        profile.about = data['about']
        profile.image = files['avatar']
        profile.save()
        return redirect('profile')

    return render(request, 'profiles/edit.html')


"""
создать страницу добавления стрима
создать класс для формы добавления стрима
name, game, is_live, preview

создать функцию для отрисовки страницы создания стрима
сделать для функции ссылку
ссылку вызвать для кнопки старт лайв стрим
"""