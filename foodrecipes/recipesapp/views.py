from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    catagories = models.Catagory.objects.all()
    context = {
        'catagories': catagories
    }
    return render(request, 'home.html', context)


class CatagoryListView(ListView):
    model = models.Catagory
    template_name = 'home.html'
    context_object_name = 'catagories'


class CatagoryDetailView(DetailView):
    model = models.Catagory
    template_name = 'catagory_detail.html'


class CatagoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Catagory
    fields = ['title', 'description', 'image']
    template_name = 'catagory_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CatagoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Catagory
    fields = ['title', 'description']
    template_name = 'catagory_form.html'

    def test_func(self):
        catagory = self.get_object()
        if self.request.user == catagory.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CatagoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Catagory
    success_url = reverse_lazy('catagories-home')
    template_name = 'catagory_confirm_delete.html'

    def test_func(self):
        catagory = self.get_object()
        if self.request.user == catagory.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About us page'})

# Recipes Views


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'home.html', context)


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'home-rec.html', context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'home-rec.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'ingredients', 'image']
    template_name = 'recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'ingredients', 'image']
    template_name = 'recipe_form.html'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')
    template_name = 'recipe_confirm_delete.html'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About us page'})

# Ingredients Views


def home(request):
    ingredients = models.Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'home-ing.html', context)


class IngredientListView(ListView):
    model = models.Ingredient
    template_name = 'home-ing.html'
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = models.Ingredient
    template_name = 'ingredient_detail.html'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = models.Ingredient
    fields = ['title', 'description', 'catagory']
    template_name = 'ingredient_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Ingredient
    fields = ['title', 'description', 'catagory']
    template_name = 'ingredient_form.html'

    def test_func(self):
        ingredient = self.get_object()
        if self.request.user == ingredient.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Ingredient
    success_url = reverse_lazy('ingredients-home')
    template_name = 'ingredient_confirm_delete.html'

    def test_func(self):
        ingredient = self.get_object()
        if self.request.user == ingredient.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About us page'})
