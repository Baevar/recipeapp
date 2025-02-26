from django.shortcuts import render
from django.http import HttpRequest, Http404
from recipeapp.models import Recipe, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from recipeapp.forms import RecipeForm
from django.db.models import Q
import random


def recipe_index(request: HttpRequest):
    
    data = Recipe.objects.all()
    if data:
        recipes = [random.choice(data) for _ in range(5)]
        context = {"recipes": recipes}    
    else:
        context = None
    return render(request, "recipeapp/recipe_index.html",context=context)


class RecipeListView(ListView):
    paginate_by = 10
    template_name = "recipeapp/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        queryset = Recipe.objects.prefetch_related("categories")
        search_query = self.request.GET.get("q")  
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset


class RecipeDetailsView(DetailView):
    template_name = "recipeapp/recipe_detail.html"
    queryset = (
        Recipe.objects.
        prefetch_related("categories")
    )
    context_object_name = "recipe"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user.pk
        context["description_short"] = Recipe.description_short
        return context
    
        


class RecipeCreateView(LoginRequiredMixin, CreateView):
       
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("recipeapp:recipe_list")
    
    def form_valid(self, form):
       
        form.instance.author = self.request.user 
        return super().form_valid(form)
        


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = "_update_form"

    def get_object(self, queryset=None):
        # Получаем объект рецепта по pk
        recipe = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь автором рецепта
        if recipe.author != self.request.user:
            raise Http404("Вы не можете редактировать этот рецепт.")  # Или можно использовать PermissionDenied
        return recipe
    
    def get_success_url(self):
        return reverse(
            "recipeapp:recipe_detail",
            kwargs={"pk": self.object.pk}
        )


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipeapp:recipe_list")
    template_name_suffix = "_delete_form"
    
    def get_object(self, queryset=None):
        # Получаем объект рецепта по pk
        recipe = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь автором рецепта
        if recipe.author != self.request.user:
            raise Http404("Вы не можете редактировать эту категорию.")  # Или можно использовать PermissionDenied
        return recipe


class CategoryListView(ListView):
    paginate_by = 10
    template_name = "recipeapp/category_list.html"
    # model = Category
    queryset = (
        Category.objects.
        prefetch_related("recipes")
    )
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    template_name = "recipeapp/category_detail.html"
    # model = Category
    queryset = (
        Category.objects.
        prefetch_related("recipes")
    )
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user.pk
        return context


class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    fields = "title", "description"
     
    success_url = reverse_lazy("recipeapp:category_list")
    template_name_suffix = "_create_form"
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = "title", "description"
    template_name_suffix = "_update_form"

    def get_object(self, queryset=None):
        # Получаем объект рецепта по pk
        recipe = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь автором рецепта
        if recipe.author != self.request.user:
            raise Http404("Вы не можете редактировать эту категорию.")  # Или можно использовать PermissionDenied
        return recipe

    def get_success_url(self):
        return reverse(
            "recipeapp:category_detail",
            kwargs={"pk": self.object.pk}
        )


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("recipeapp:category_list")
    template_name_suffix = "_delete_form"

    def get_object(self, queryset=None):
        # Получаем объект рецепта по pk
        recipe = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь автором рецепта
        if recipe.author != self.request.user:
            raise Http404("Вы не можете редактировать эту категорию.")  # Или можно использовать PermissionDenied
        return recipe


