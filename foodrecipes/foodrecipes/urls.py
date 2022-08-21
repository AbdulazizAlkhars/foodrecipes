"""foodrecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from recipesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name='user-logout'),
    path('', views.CatagoryListView.as_view(), name='catagories-home'),
    path('catagory/create/', views.CatagoryCreateView.as_view(),
         name='catagories-create'),
    path('catagory/<int:pk>/',
         views.CatagoryDetailView.as_view(), name='catagories-detail'),
    path('catagory/<int:pk>/update/',
         views.CatagoryUpdateView.as_view(), name='catagories-update'),
    path('catagory/<int:pk>/delete/',
         views.CatagoryDeleteView.as_view(), name='catagories-delete'),

    #     Recipes URLS
    path('recipe-list/', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipe/<int:pk>/',
         views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('recipe/<int:pk>/update/',
         views.RecipeUpdateView.as_view(), name='recipes-update'),
    path('recipe/<int:pk>/delete/',
         views.RecipeDeleteView.as_view(), name='recipes-delete'),
    path('about-recipe/', views.about, name='recipes-about'),

    #    Ingredients URLS

    path('ingredient-list/', views.IngredientListView.as_view(),
         name='ingredients-home'),
    path('ingredient/create/', views.IngredientCreateView.as_view(),
         name='ingredients-create'),
    path('ingredient/<int:pk>/',
         views.IngredientDetailView.as_view(), name='ingredients-detail'),
    path('ingredient/<int:pk>/update/',
         views.IngredientUpdateView.as_view(), name='ingredients-update'),
    path('ingredient/<int:pk>/delete/',
         views.IngredientDeleteView.as_view(), name='ingredients-delete'),
    path('about-ingredient/', views.about, name='ingredients-about'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
