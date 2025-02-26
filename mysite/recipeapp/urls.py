from django.urls import path
from recipeapp.views import (recipe_index, RecipeListView, CategoryListView,
                             RecipeDetailsView, CategoryDetailView, RecipeCreateView,
                             CategoryCreateView, RecipeUpdateView, CategoryUpdateView,
                             RecipeDeleteView, CategoryDeleteView)

app_name = "recipeapp"

urlpatterns = [
    path("", recipe_index, name="recipe_index"),
    path("recipe/list", RecipeListView.as_view(), name="recipe_list"),
    path("recipe/category", CategoryListView.as_view(), name="category_list"),
    path("recipe/<int:pk>", RecipeDetailsView.as_view(), name="recipe_detail"),
    path("recipe/category/<int:pk>",
         CategoryDetailView.as_view(), name="category_detail"),
    path("recipe/create", RecipeCreateView.as_view(), name="create_recipe"),
    path("recipe/category/create",
         CategoryCreateView.as_view(), name="create_category"),
    path("recipe/<int:pk>/update", RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipe/category/<int:pk>/update", CategoryUpdateView.as_view(), name="category_update"),
    path("recipe/<int:pk>/delete", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("recipe/category/<int:pk>/delete", CategoryDeleteView.as_view(), name="category_delete"),
]
