from django.views.generic import ListView
from recipes.models import Recipe

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class HomePageView(ListView):
    model = Recipe
    template_name = 'home.html'

def register_view(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'registration/register.html', {'form': form})
