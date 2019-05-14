from django.urls import path

from pages.views import HomePageView
from recipes.views import recipe_detail_view, recipe_share_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('share/', recipe_share_view.as_view()),
    path('<int:pk>/', recipe_detail_view.as_view(), name='detail'),
]
