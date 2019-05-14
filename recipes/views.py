from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .forms import RecipeForm
from .models import Recipe

class recipe_share_view(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe/share_recipe.html'
    success_url = reverse_lazy('home')

class recipe_detail_view(View):
    model = Recipe
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
        context = {'recipe': recipe}
        return render(request, 'recipe/recipe_details.html', context)
